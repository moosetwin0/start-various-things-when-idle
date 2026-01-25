# start-various-things-when-idle Linux v2



import os # a lot of stuff
import configparser
from time import sleep
from sys import argv # to check for debug flag # !!! can be removed if unused
import psutil # checking if a process is running
from subprocess import Popen # to open/close programs
from FullscreenDetector import window_is_fullscreen
from Xlib.display import Display # for getting pointer position, already needed by FullscreenDetector anyways

# I initially copied it from https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/ but now that I know what I know I could do it myself
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower() and processName != '':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# running executables blacklist
def blacklisted():
    if checkIfProcessRunning(config['misc']['blacklist 1']) or checkIfProcessRunning(config['misc']['blacklist 2']) or checkIfProcessRunning(config['misc']['blacklist 3']):
        return True
    else: return False

# !!! can remove later if unused
debug = False # stays False if no arg is given or arg is not '--debug'
try: 
    # check for debug flag
    if argv[1].lower() == '--debug': # if first argument is '--debug'
        debug = True
except IndexError: pass

# check for vscodium debug environment
if ('TERM_PROGRAM' in os.environ.keys() and os.environ['TERM_PROGRAM'] == 'vscode'):
    debug = True

def getmousepos(): # shorthand
    mouseinfo = Display().screen().root.query_pointer() # probably could merge this line with the return but idk how
    return mouseinfo.root_x, mouseinfo.root_y

config = configparser.ConfigParser(allow_no_value=True)

# checks if config file exists, if it doesn't, create new one with the below defaults, if it does, read it
while True: # for updating config file
    if not os.path.isfile('cfg.ini'):
        # defaults
        # basedpyright gives a reportArgumentType error here but the code works fine
        # !!! couldn't get wireguard to work so it is commented out, and qbittorrent is too for safety reasons
        config['toggles'] = {'don\'t go idle while in fullscreen':True,  # pyright: ignore[reportArgumentType]
                            #'wireguard':'on', 
                            #'qbittorrent':'on',
                            'VM':'on',
                            'ytdlp':'on'}
        config['paths'] = {'# the paths for any unused features can be left blank':None,  # pyright: ignore[reportArgumentType]
                        #'wireguard config name':'wgcf-profile', 
                        'ytdlp path':'~/Music/yt-dlp/yt-dlp'}
        config['misc'] = {'vm name':'archiveteam-warrior-4.2',  # pyright: ignore[reportArgumentType]
                        'seconds before idle':'600', 
                        '# how long it should wait before checking if the mouse has moved':None,
                        '# low values will cause performance issues!':None,
                        'seconds per poll':'5',
                        '# do not go idle if the following processes are running':None, # can't provide example because configparser can't escape delimiters
                        '# the blacklist can be left blank if not used':None,
                        'blacklist 1':'',
                        'blacklist 2':'',
                        'blacklist 3':''}
        config.write(open('cfg.ini', 'w'))
        print('The config file was not found, so a new one has been created. Edit that file to your specifications, and then press Enter to continue.')
        _ = input()
    else: 
        _ = config.read('cfg.ini')
        if debug: 
            print('config file found, it is as follows:')
            print({section: dict(config[section]) for section in config.sections()}) # taken from https://stackoverflow.com/a/50362738
    break

if debug: 
    config['misc']['seconds before idle'] = '10' # set seconds before idle to 10 seconds if in debug environment
    config['misc']['seconds per poll'] = '1'

# more optimizable code
while(True): # this is so that the idle checking still continues if the computer becomes (temporarily) active
    startpos = getmousepos()
    mousetimer = 0
    # increases mousetimer until it reaches a set value, mouse movement resets it to 0
    while(mousetimer < int(config['misc']['seconds before idle'])): # runs code until mouse is still for time-before-idle seconds
        # the below two if statements could probably be merged, TODO
        if startpos != getmousepos(): # if mouse has moved
            mousetimer = 0
            startpos = getmousepos()
        # having it only check the var once (instead of every loop) might be better on performance but it'd be more complicated
        if (config['toggles'].getboolean('don\'t go idle while in fullscreen') and window_is_fullscreen()) or blacklisted():
            if debug: print(f'-- fullscreen: {window_is_fullscreen()}, blacklisted: {blacklisted()} --')
            mousetimer = 0
            # mousetimer will constantly be at 1 if fullscreen because of above and below but it does not matter
        if debug: print(mousetimer)
        mousetimer += int(config['misc']['seconds per poll'])
        sleep(int(config['misc']['seconds per poll']))

    # split() is used to prevent error when passing multiple args
    # these could be done without the repeated if statements but I can't be bothered
    # apparently True != 'True' and I wish I knew that yesterday before I changed all the code
    # `_ =` is used to prevent printing '<os._wrap_close object>' for every process
    startpos = getmousepos() # for later
    # !!! fix wireguard sudo, see changelog
    #if config['toggles'].getboolean('wireguard'):
        #_ = Popen(f"sudo wg-quick up {config['paths']['wireguard config name']}".split())
    #if config['toggles'].getboolean('qbittorrent'):
        # qbittorrent process is saved to be killed later
        #qbit = Popen('flatpak run org.qbittorrent.qBittorrent'.split()) # obviously flatpak-only
    if config['toggles'].getboolean('VM'):
        _ = Popen(f'virtualboxvm --startvm {config['misc']['vm name']}'.split())
    if config['toggles'].getboolean('ytdlp'): 
        # subprocess doesn't work with ~/ so expanduser is used
        ytdlppath = os.path.expanduser(config['paths']['ytdlp path'])
        _ = Popen(ytdlppath, cwd=os.path.dirname(ytdlppath))
    sleep(5)
    _ = Popen('xset dpms force standby', shell=True) # manually turn off the monitor, otherwise programs would keep it on

    # for closing programs when coming out of idle, adapted from stackoverflow
    # also could be done without the repeated if statements, TODO
    while(True):
        if startpos != getmousepos():
            if debug: print('-- shutting down --')
            if config['toggles'].getboolean('VM'):
                _ = Popen(f'vboxmanage controlvm {config['misc']['vm name']} acpipowerbutton'.split())
            # !!! fix wireguard sudo, see changelog
            #if config['toggles'].getboolean('qbittorrent'):
                #qbit.terminate() # pyright: ignore[reportPossiblyUnboundVariable]
            #if config['toggles'].getboolean('wireguard'):
                #_ = Popen(f"sudo wg-quick down {config['paths']['wireguard config name']}".split())
            break
        sleep(int(config['misc']['seconds per poll'])) 

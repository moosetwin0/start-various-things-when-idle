import os
import win32api
import win32gui
import configparser
from ctypes import windll
from time import sleep
import savepagenow

# check if running in vscode and if so set working directory so I can debug in vscode without random errors
# also stolen from stackoverflow
if 'TERM_PROGRAM' in os.environ.keys() and os.environ['TERM_PROGRAM'] == 'vscode':
    os.chdir(os.path.expanduser('~\\Desktop\\Code'))


# check if window is fullscreen
# this was originally stolen from stackoverflow but it didn't work correctly so I stole it from chatgpt instead
def is_fullscreen():
    active_window = win32gui.GetForegroundWindow()
    window_rect = win32gui.GetWindowRect(active_window)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    return width == screen_width and height == screen_height

config = configparser.ConfigParser(allow_no_value=True)

# checks if config file exists, if it doesn't, create new one with booleanss, if it does, read it
if not os.path.isfile('cfg.ini'):
    # defauits
    config['booleans'] = {'# change to True for on, False for off':None, 
                          'do not detect idle while fullscreen':True,
                          'wireguard on/off':'True', 
                          'wireguard turns off after idle ends':'True', 
                          'qbittorrent on/off':True, 
                          'qbittorrent turns off after idle ends':True, 
                          'archiveteam VM on/off':True, 
                          'archiveteam VM turns off after idle ends':True, 
                          'ytsync on/off':True}
    config['paths'] = {'# you do not need to fill in ones that are turned off in the boolean section!':None, 
                       'wireguard executable path':r'C:\Program Files\WireGuard\wireguard.exe', 
                       'wireguard config path':r'C:\Program Files\WireGuard\Data\Configurations\wgcf-profile.conf.dpapi', 
                       'qbittorrent executable path':r'C:\Program Files\qBittorrent\qbittorrent.exe', 
                       'virtualbox executable path':r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe', 
                       'ytsync path':r'G:\music\playlist sync.lnk'}
    config['misc'] = {'archiveteam warrior vm name':'archiveteam-warrior-3.2', 
                      '# the duration should be in seconds':None, 
                      'time before idle':'600', 
                      '# leave blank to turn off single web page archiving':None,
                      '# example: "URL 1 = https://www.google.com/"':None,
                      'URL 1':'',
                      'URL 2':'',
                      'URL 3':''}
    # creating file requires admin, reading might too
    config.write(open('cfg.ini', 'w'))
else: config.read('cfg.ini')

while(True): # this is so that the idle checking still continues if the computer becomes (temporarily) active
    fixedposition = win32api.GetCursorPos() # a lot of this type of code could probably be put into a dedicated function but I can't be bothered
    mousetimer = 0
    # increases mousetimer until it reaches a set value, mouse movement resets it to 0
    while(mousetimer < int(config['misc']['time before idle'])):
        position = win32api.GetCursorPos()
        if fixedposition != position:
            mousetimer = 0
            fixedposition = win32api.GetCursorPos()
        if config['booleans']['do not detect idle while fullscreen'] == 'True' and is_fullscreen():
            mousetimer = 0
            # mousetimer will constantly be at 0.05 if fullscreen because of above and below but it does not matter
        mousetimer = round((mousetimer + 0.05), 2) # rounding is to remove floating point errors, not very important but it looks nice
        sleep(0.05)

    # runs the programs, REQUIRES ADMIN
    # these should be done without the repeated if statements but I (mistakenly) thought it wouldn't matter
    # subprocess doesn't like working in the background so popen is used instead
    # apparently True != 'True' and I wish I knew that yesterday before I changed all the code
    if config['booleans']['wireguard on/off'] == 'True':
        os.popen(fr'"{config['paths']['wireguard executable path']}" /installtunnelservice "{config['paths']['wireguard config path']}"')
    if config['booleans']['qbittorrent on/off'] == 'True':
        os.popen(fr'"{config['paths']['qbittorrent executable path']}"')
    if config['booleans']['archiveteam VM on/off'] == 'True':
        os.popen(fr'"{config['paths']['virtualbox executable path']}" startvm "{config['misc']['archiveteam warrior vm name']}"')
    if config['booleans']['ytsync on/off'] == 'True':
        os.popen(fr'"{config['paths']['ytsync path']}"')
    # I tried to make this just loop 3 times but I got overwhelmed so you get more redundant code
    if config['misc']['URL 1']:
        savepagenow.capture_or_cache(config['misc']['URL 1'])
    if config['misc']['URL 2']:
        savepagenow.capture_or_cache(f'{config['misc']['URL 2']}')
    if config['misc']['URL 3']:
        savepagenow.capture_or_cache(f'{config['misc']['URL 3']}')

    # for closing programs when coming out of idle, adapted from stackoverflow
    # also could be done without the repeated if statements
    fixedposition = win32api.GetCursorPos()
    while(True):
        position = win32api.GetCursorPos()
        if fixedposition != position: # this code also requires admin unfortunately
            if config['booleans']['archiveteam VM turns off after idle ends'] == 'True':
                os.popen(fr'"{config['paths']['virtualbox executable path']}" controlvm "{config['misc']['archiveteam warrior vm name']}" acpipowerbutton')
            if config['booleans']['qbittorrent turns off after idle ends'] == 'True':
                os.popen('taskkill /im "qbittorrent.exe"')
            if config['booleans']['wireguard turns off after idle ends'] == 'True':
                os.popen(fr'"{config['paths']['wireguard executable path']}" /uninstalltunnelservice "{config['paths']['wireguard config path']}"')
            break
        sleep(0.05)

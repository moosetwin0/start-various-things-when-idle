import os
import win32api
import configparser
from time import sleep
import subprocess

config = configparser.ConfigParser(allow_no_value=True)

# checks if config file exists, if it doesn't, create new one with booleanss, if it does, read it
if not os.path.isfile('cfg.ini'):
    # defauits
    config['booleans'] = {'# change to 1 for on, 0 for off':None, 'wireguard':'1', 'wireguard turns off after idle ends':'1', 'qbittorrent':'1', 'qbittorrent turns off after idle ends':'1', 'archiveteam VM':'1', 'archiveteam VM turns off after idle ends':'1', 'ytsync':'1'}
    config['paths'] = {'# you do not need to fill in ones that are turned off in the boolean section!':None, 'wireguard executable path':r'C:\Program Files\WireGuard\wireguard.exe', 'wireguard config path':r'C:\Program Files\WireGuard\Data\Configurations\wgcf-profile.conf.dpapi', 'qbittorrent executable path':r'C:\Program Files\qBittorrent\qbittorrent.exe', 'virtualbox executable path':r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe', 'ytsync path':r'G:\music\playlist sync.lnk'}
    config['misc'] = {'archiveteam warrior vm name':'archiveteam-warrior-3.2', '# the duration should be in seconds':None, 'time before idle':'1200'}
    # creating file requires admin, reading might too
    config.write(open('cfg.ini', 'w'))
else: config.read('cfg.ini')

while(True): # this is so that the idle checking still continues if the computer becomes temporarily active
    fixedposition = win32api.GetCursorPos() # a lot of this type of code could probably be put into a dedicated function but I can't be bothered
    mousetimer = 0
    # increases mousetimer until it reaches a set value, mouse movement resets it to 0
    while(mousetimer < int(config['misc']['time before idle'])):
        position = win32api.GetCursorPos()
        if fixedposition != position:
            mousetimer = 0
            fixedposition = win32api.GetCursorPos()
        mousetimer = round((mousetimer + 0.05), 2) # rounding is to remove floating point errors, not very important but it looks nice
        sleep(0.05)

    # runs the programs, REQUIRES ADMIN
    # these should be done without the repeated if statements but I (mistakenly) thought it wouldn't matter
    # subprocess doesn't like working in the background so it is commented out
    if int(config['booleans']['wireguard']) == 1:
        os.popen(fr'"{config['paths']['wireguard executable path']}" /installtunnelservice "{config['paths']['wireguard config path']}"')
        # subprocess.Popen(fr'"{config['paths']['wireguard executable path']}" /installtunnelservice "{config['paths']['wireguard config path']}"',shell=False, stdin=None, stdout=None, stderr=None)
    if int(config['booleans']['qbittorrent']) == 1:
        os.popen(fr'"{config['paths']['qbittorrent executable path']}"')
        # subprocess.Popen(fr'"{config['paths']['qbittorrent executable path']}"',shell=False, stdin=None, stdout=None, stderr=None)
    if int(config['booleans']['archiveteam VM']) == 1:
        os.popen(fr'"{config['paths']['virtualbox executable path']}" startvm "{config['misc']['archiveteam warrior vm name']}"')
        # subprocess.Popen(fr'"{config['paths']['virtualbox executable path']}" startvm "{config['misc']['archiveteam warrior vm name']}"',shell=False, stdin=None, stdout=None, stderr=None)
    if int(config['booleans']['ytsync']) == 1:
        os.popen(fr'"{config['paths']['ytsync path']}"')
        # subprocess.Popen(fr'"{config['paths']['ytsync path']}"',shell=True, stdin=None, stdout=None, stderr=None)

    # for closing programs when coming out of idle, shamefully stolen from stackoverflow
    # also could be done without the repeated if statements
    fixedposition = win32api.GetCursorPos()
    while(True):
        position = win32api.GetCursorPos()
        if fixedposition != position: # this code also requires admin unfortunately
            if int(config['booleans']['archiveteam VM turns off after idle ends']) == 1:
                os.popen(fr'"{config['paths']['virtualbox executable path']}" controlvm "{config['misc']['archiveteam warrior vm name']}" acpipowerbutton')
                # subprocess.Popen(fr'"{config['paths']['virtualbox executable path']}" controlvm "{config['misc']['archiveteam warrior vm name']}" acpipowerbutton',shell=False, stdin=None, stdout = None, stderr=None)
            if int(config['booleans']['qbittorrent turns off after idle ends']) == 1:
                os.popen('taskkill /im "qbittorrent.exe"')
                # subprocess.Popen('taskkill /im "qbittorrent.exe"',shell=False, stdin=None, stdout=None, stderr=None)
            if int(config['booleans']['wireguard turns off after idle ends']) == 1:
                os.popen(fr'"{config['paths']['wireguard executable path']}" /uninstalltunnelservice "{config['paths']['wireguard config path']}"')
                # subprocess.Popen(fr'"{config['paths']['wireguard executable path']}" /uninstalltunnelservice "{config['paths']['wireguard config path']}"',shell=False, stdin=None, stdout=None, stderr=None)
            break
        sleep(0.05)

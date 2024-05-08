import os
import win32api
from time import sleep

# important! 
# replace the below text where shown with the actual names/paths for the files 
# replace \ with \\ or python will get confused
# the replaced text must be in quotes "like this", see example
wgcf = "REPLACE THIS TEXT WITH WIREGUARD CONFIG PATH" # example: "C:\\Program Files\\WireGuard\\Data\\Configurations\\wgcf-profile.conf.dpapi"
atvm = "REPLACE THIS TEXT WITH THE NAME OF THE ARCHIVETEAM VM" # example: "archiveteam-warrior-3.2"

while(True): # this is so that the idle checking still continues if the computer becomes temporarily active

    fixedposition = win32api.GetCursorPos() # a lot of this type of code could probably be put into a dedicated function but I can't be bothered
    mousetimer = 0

    while(mousetimer < 600): #default is 600 seconds (10 minutes), can be changed to your preference
        position = win32api.GetCursorPos()
        if fixedposition != position:
            mousetimer = 0
            fixedposition = win32api.GetCursorPos()
        sleep(0.05)
        mousetimer = round((mousetimer + 0.05), 2) # rounding is to remove floating point errors, not very important but it looks nice

    # runs the programs, REQUIRES ADMIN, assumes the paths are the default which may change in future updates
    os.popen(f'"C:\\Program Files\\WireGuard\\wireguard.exe" /installtunnelservice "{wgcf}"')
    os.popen('"C:\\Program Files\\qBittorrent\\qbittorrent.exe"')
    os.popen(f'"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" startvm "{atvm}"')

    # for closing programs when coming out of idle, shamefully stolen from stackoverflow
    fixedposition = win32api.GetCursorPos()
    while(True):
        position = win32api.GetCursorPos()
        if fixedposition != position: # this code also requires admin unfortunately
            os.popen(f'"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" controlvm "{atvm}" acpipowerbutton')
            os.popen('taskkill /im "qbittorrent.exe"')
            # comment the below if you don't want it to turn off the vpn when computer becomes active
            os.popen(f'"C:\\Program Files\\WireGuard\\wireguard.exe" /uninstalltunnelservice "{atvm}"')
            break
        sleep(0.05)

import os
import win32api
from time import sleep

# important! 
# replace text where shown with the actual names/paths for the files 
# replace \ with \\ or python will get confused
# the replaced text must be in quotes "like this"
wgcf = "REPLACE THIS TEXT WITH WIREGUARD PATH" # example: "C:\\Program Files\\WireGuard\\Data\\Configurations\\wgcf-profile.conf.dpapi"
atvm = "REPLACE THIS TEXT WITH THE NAME OF THE ARCHIVETEAM VM" # example: "archiveteam-warrior-3.2"

# runs the programs, assumes that you are actually idle
os.popen(f'"C:\\Program Files\\WireGuard\\wireguard.exe" /installtunnelservice "{wgp}"')
os.popen('"C:\\Program Files\\qBittorrent\\qbittorrent.exe"')
os.popen(f'"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" startvm "{atvm}"')

# for closing programs when coming out of idle, shamefully stolen from stackoverflow
fixedposition = win32api.GetCursorPos()
while(True):
    position = win32api.GetCursorPos()
    if fixedposition != position:
        os.popen(f'"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" controlvm "{atvm}" acpipowerbutton')
        os.popen('taskkill /im "qbittorrent.exe"')
        os.popen(f'"C:\\Program Files\\WireGuard\\wireguard.exe" /uninstalltunnelservice "{wgp}"')
        exit()
    sleep(0.05)

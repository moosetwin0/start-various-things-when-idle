import os
import win32api
from time import sleep

# runs programs, assumes that you are actually idle
os.popen('"C:\\Program Files\\WireGuard\\wireguard.exe" /installtunnelservice "C:\\Program Files\\WireGuard\\Data\\Configurations\\wgcf-profile.conf.dpapi"')
os.popen('"C:\\Program Files\\qBittorrent\\qbittorrent.exe"')
os.popen('"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" startvm "archiveteam-warrior-3.2"')

# for closing programs when coming out of idle, shamefully stolen from stackoverflow
fixedposition = win32api.GetCursorPos()
while(True):
    position = win32api.GetCursorPos()
    if fixedposition != position:
        os.popen('"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" controlvm "archiveteam-warrior-3.2" acpipowerbutton')
        os.popen('taskkill /im "qbittorrent.exe"')
        exit()
    sleep(0.05)
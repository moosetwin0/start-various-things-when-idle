# start various things when idle

**I no longer use Windows, so the Windows build will no longer be maintained.**

This is designed for Linux Mint, but other Ubuntu-based distros will probably also work.

This was built assuming you are using the flatpak version of qbittorrent, and the executable version of yt-dlp.

This project requires the modules Xlib and psutil to be installed.

Thank you to The King Killer for the fullscreen detector script.

The code for checking if the display is in fullscreen has a different license, CC BY-SA 4.0. I'm pretty sure mixing licenses like this is fine due to GPLv3 being ShareAlike compatible, but I am not a lawyer. If there is anything I should know regarding this, please tell me.

> [!TIP]
> I recommended running this whenever your computer starts, it's what I do anyways

TODO:
- fix wireguard and qbittorrent functionality !!!
- Detect if mouse moves soon after opening archiveteam VM, and force shutdown if so (soft shutdown does not work soon after starting VMs)
- Detect config changes and *ask user* if they want to restart program
- Detect invalid config file and tell user
- Detect dangerous settings (other) and tell user
- check github for updates? I dunno
  - automatically update config file somehow
- test and get it working on flatpak/non-flatpak versions of programs

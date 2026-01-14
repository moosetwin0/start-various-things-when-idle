# start various things when idle

**I no longer use Windows, so the Windows build will no longer be maintained.**

This is designed for Linux Mint, but other Ubuntu-based distros will probably also work.

This was built assuming you are using the flatpak version of qbittorrent, and the executable version of yt-dlp.

This project requires the modules Xlib and psutil to be installed.

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

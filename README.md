# start various things when idle

**I no longer use Windows, so the Windows build will no longer be maintained.**

This is designed for Linux Mint, but other Ubuntu-based distros will probably also work.

This was built assuming you are using the flatpak version of qbittorrent, and the executable version of yt-dlp.

This project requires the modules Xlib and psutil to be installed

> [!CAUTION] 
> qBittorrent is assumed to have the settings 'Close qBittorrent to notification area' and 'Confirmation on exit when torrents are active' disabled, if they are enabled then it can continue torrenting after, potentially *without the vpn enabled*, it is also strongly recommended to [bind your torrent client to your VPN](https://redd.it/ssy8vv).
> - If this is an issue for you, you can:
>   - turn off the above two settings (!)
>   - [bind qBittorrent to your VPN](https://redd.it/ssy8vv) (!)
>   - turn off qBittorrent in the config file
>   - keep the VPN on, also in the config file
>   - stop committing copyright infringement!

> [!TIP]
> I recommended running this whenever your computer starts, it's what I do anyways

TODO:
- Detect if mouse moves soon after opening archiveteam VM, and force shutdown if so (soft shutdown does not work soon after starting VMs)
- Detect config changes and *ask user* if they want to restart program
- Detect invalid config file and tell user
- Detect dangerous settings (other) and tell user
- check github for updates? I dunno
  - automatically update config file somehow
- test and get it working on flatpak/non-flatpak versions of programs

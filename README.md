# start various things when idle

**I no longer use Windows, so this has been archived.**

> [!CAUTION] 
> qBittorrent is assumed to have the settings 'Close qBittorrent to notification area' and 'Confirmation on exit when torrents are active' disabled, if they are enabled then it can continue torrenting after, potentially **WITHOUT THE VPN ENABLED**, it is also strongly recommended to [bind your torrent client to your VPN](https://redd.it/ssy8vv).
> - If this is an issue for you, you can:
>   - turn off the above two settings (!)
>   - [bind qBittorrent to your VPN](https://redd.it/ssy8vv) (!)
>   - turn off qBittorrent in the config file
>   - keep the VPN on, also in the config file
>   - stop torrenting stuff that'll get you in trouble!

> [!NOTE]
> The SavePageNow module does not work with Task Scheduler, if you use it with Task Scheduler this will cause the program to get stuck forever: turn off single web page archiving in the config file if you want to use this script with it
>
> This requires administrator permissions for a lot of things (see code if you are worried)
>
> Apon first start, the script will create a config file and then exit, configure that and then start the program again.

> [!TIP]
> I recommended running this whenever your computer starts, I use Task Scheduler for this

TODO:
- Detect if mouse moves soon after opening archiveteam VM, and force shutdown if so (soft shutdown does not work soon after starting VMs)
- Add config option for opening in background, useful for when screensaver time does not match config time
  - Look into CLIs or python modules for qbittorrent and wireguard
- Detect config changes and *ask user* if they want to restart program
- Detect if run without administrator permissions and tell user
- Detect invalid config file and tell user
- Detect dangerous settings (other) and tell user
- check github for updates? idfk
  - automatically update config file somehow

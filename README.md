# start various things when idle

⚠️WARNING! qBittorrent is assumed to have the setting 'Close qBittorrent to notification area' and 'Confirmation on exit when torrents are active' disabled, if it is enabled then it can continue torrenting after, potentially WITHOUT THE VPN ENABLED, it is also strongly recommended to [bind your torrent client to your VPN](https://redd.it/ssy8vv).
- If you are worried about this, you can:
  - [bind your client to your VPN](https://redd.it/ssy8vv) 
  - turn off qBittorrent in the config file
  - keep the VPN on, also in the config file

This requires administrator permissions for starting/stopping programs, (see code if you are worried) 

It is recommended to run this code whenever your computer starts, I use Task Scheduler for this
I recommend starting once and then changing config file to match preference

TODO:
- Add config option for opening in background, useful for when screensaver time does not match config time
  - Look into CLIs or python modules for qbittorrent and wireguard
- Detect config changes and ask user if they want to restart program
- Detect if run without administrator permissions and tell user
- Detect invalid config file and tell user
- Detect dangerous settings (other) and tell user
- Fix unclear wording in config file, specifically to mention that '<name> = %' means opening or not opening <name>
- Config option to not open when something is fullscreen, so that it stops opening while I'm watching a video
  - Config option to either open % seconds later apon exiting fullscreen or just to reset mousetimer
- Check github for updates? idfk

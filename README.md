# start various things when idle

WARNING! qBittorrent is assumed to have the setting 'Close qBittorrent to notification area' and 'Confirmation on exit when torrents are active' disabled, if it is enabled then it can continue torrenting after, potentially WITHOUT THE VPN ENABLED
- If you are worried about this, you can turn off qBittorrent in the config file, or keep the VPN on, also in the config file

this requires administrator permissions for wireguard and taskkill, (see code if you are worried) 
it is recommended to run this code whenever your computer starts, I use Task Scheduler for this

I recommend starting once and then changing config file to match preference

TODO:
- Add messagebox asking user if they want to restart when detecting config changes
- Add config option for opening in background, useful for when screensaver time does not match config time
- Detect if run without administrator permissions and tell user
- Detect invalid config file and tell user
- Detect dangerous settings (other) and tell user
- Fix unclear wording in config file, specifically to mention that '<name> = %' means opening or not opening <name>

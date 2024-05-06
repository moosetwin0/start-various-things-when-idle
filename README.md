# start the vpn, torrent client, and archiveteam warrior vm when idle

before first start you need to replace some parts of the python code where mentioned

to automatically start when idle you need to make a task scheduler file set to waiting 10 minutes, (or however long you want your computer to be idle before it runs) I might add a pre-made one to the repository when I have the energy

this also requires administrator permissions for wireguard and taskkill, (see code if you want) make sure you give it to the task scheduler file when you create it

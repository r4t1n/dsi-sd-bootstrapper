# dsi-sd-bootstrapper

These Python scrips will get your SD card bootstrapped for homebrewing your Nintendo DSi! While using it them should follow along with this guide: https://dsi.cfw.guide/get-started.html

## config.ini

Before running any scripts you should edit the `config.ini` file, most of the options are simple True and False options to bootstrap the chosen program. Here's an example:

```
[Options]
sdRoot =

; Refer to: https://dsi.cfw.guide/get-started.html#section-i-prep-work
; Memory Pit Facebook Icon: https://dsi.cfw.guide/launching-the-exploit.html#section-i-checking-your-dsi-camera-version
[Bootstrap]
twilightMenu = true
dumpTool = true
memoryPit = true
memoryPitFacebookIcon = true
flipnoteLenny = false
unlaunch = true
godmode9i = false

; Refer to: https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card
[Cleanup]
memoryPit = true
flipnoteLenny = false
flipnoteLennyRegion =
unlaunch = true
```

## bootstrap.py

### Running

To run the script simply run either command:

```
./bootstrap.py
```

***or***

```
python3 bootstrap.py
```

### Flipnote Lenny

Currently the Flipnote Lenny private folder you need to use the exploit has been packaged in this Git repository, this is because the download link is not a direct URL but a JavaScript event that requires you interact with the website. If anyone has a solution you are welcome to contribute! https://davejmurphy.com/%CD%A1-%CD%9C%CA%96-%CD%A1/

(I believe it's okay since the zip archive has not been updated since June 6, 2018)

## cleanup.py

This cleanup script will remove unneunnecessary files from your SD card after the bootstrap, clearing up space! The running part is the same as the bootstrap script

# dsi-sd-bootstrapper

These Python scrips will get your SD card bootstrapped for homebrewing your Nintendo DSi! While using it them should follow along with this guide: https://dsi.cfw.guide/get-started.html

## config.ini

Before running any scripts you should edit the `config.toml` file, most of the options are simple true and false values to bootstrap the chosen program. Here's an example:

```
[options]
sd_root = ""

# Refer to: https://dsi.cfw.guide/get-started.html
[bootstrap]
twilight_menu = true
dumptool = true
memory_pit = true
memory_pit_facebook_icon = true # https://dsi.cfw.guide/launching-the-exploit.html#section-i-checking-your-dsi-camera-version
flipnote_lenny = false
unlaunch = true
godmode9i = false

# Refer to: https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card
[cleanup]
memory_pit = true
flipnote_lenny = false
flipnote_lenny_region = "" # https://dsi.cfw.guide/installing-unlaunch.html?tab=flipnote-lenny#section-iii-post-unlaunch-configuration
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

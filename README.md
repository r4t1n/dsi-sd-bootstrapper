# dsi-sd-bootstrapper

These Python scrips will get your SD card bootstrapped for homebrewing your Nintendo DSi! While using it them should follow along with this guide: https://dsi.cfw.guide/get-started.html

## config.ini

Before running any scripts you should edit the `config.ini` file, most of the options are simple True and False options to bootstrap the chosen program. Here's an example:

```
[Settings]
sd_root = /mnt/sd_card

[Bootstrap Stage I]
twilight_menu = True
dumptool = True

[Bootstrap Stage II]
memory_pit = True
memory_pit_facebook_icon = True
flipnote_lenny = False

[Bootstrap Stage III]
unlaunch = True
godmode9i = False

[Cleanup]
memory_pit = True
flipnote_lenny = False
flipnote_lenny_region = Europe/Australia
unlaunch = True
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

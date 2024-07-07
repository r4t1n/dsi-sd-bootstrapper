#!/usr/bin/env python3

# This cleanup script follows this guide:
# https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card

import utils

config = utils.get_config()
tmp_directory = "/tmp/dsi-bootstrap"


def main():
    print(
        ":: This script will perform an SD card cleanup: https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card"
    )

    sd_root = utils.get_sd_root(config)

    print(":: Starting cleanup")
    cleanup(sd_root)


def cleanup(sd_root):
    if config["Cleanup"]["memory_pit"] == "True":
        memory_pit(sd_root)
    elif config["Cleanup"]["flipnote_lenny"] == "True":
        flipnote_lenny(sd_root)
    if config["Cleanup"]["unlaunch"] == "True":
        unlaunch(sd_root)


def memory_pit(sd_root):
    print(" removing Memory Pit binary from SD card...")
    pit_filepath = utils.join_path(sd_root, "private/ds/app/484E494A/pit.bin")
    utils.remove_file(pit_filepath)


def flipnote_lenny(sd_root):
    region = utils.get_flipnote_lenny_region(config)
    files = {
        1: "001/800031_104784BAB6B57_000.ppm",
        2: "001/T00031_1038C2A757B77_000.ppm",
    }
    paths = {
        1: "private/ds/app/4B47554A",
        2: "private/ds/app/4B475545",
        3: "private/ds/app/4B475556",
    }

    print(" removing other Flipnote Studio region folders...")
    for key, path in paths.items():
        if key != region:
            region_path = utils.join_path(sd_root, path)
            utils.remove_directory(region_path)

    print(" removing Flipnote Lenny PPM files...")
    for file, path in files.items():
        directory_path = utils.join_path(sd_root, paths[region])
        filepath = utils.join_path(directory_path, path)
        utils.remove_file(filepath)


def unlaunch(sd_root):
    print(" removing Unlaunch files from SD card...")
    unlaunch_path = utils.join_path(sd_root, "UNLAUNCH.DSI")
    utils.remove_file(unlaunch_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n:: Exiting...")

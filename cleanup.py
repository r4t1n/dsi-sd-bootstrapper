#!/usr/bin/env python3

# This cleanup script follows this guide:
# https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card

import utils


config = utils.config.get_config()
tmp_directory = "/tmp/dsi-bootstrap"


def main():
    print(
        f"{utils.Color.start} {utils.Color.make_bold("This script will perform an SD card cleanup")}: https://dsi.cfw.guide/installing-unlaunch.html#section-iv-cleaning-up-your-sd-card"
    )

    sd_root = utils.config.get_sd_root(config)
    print(f"{utils.Color.start} {utils.Color.make_bold("SD root path")}: {sd_root}")

    sd_root_choice = get_yes_no_input(
        f"{utils.Color.start} {utils.Color.make_bold("Is the SD root path correct? [Y/n]")} "
    )

    if not sd_root_choice:
        exit()

    print(f"{utils.Color.start} {utils.Color.make_bold("Starting cleanup...")}")
    cleanup(sd_root)

    print(f"{utils.Color.start} {utils.Color.make_bold("Cleanup complete!")}")


def cleanup(sd_root):
    if utils.config.get_option(config, "Cleanup", "memoryPit") == "true":
        memory_pit(sd_root)
    elif utils.config.get_option(config, "Cleanup", "flipnoteLenny") == "true":
        flipnote_lenny(sd_root)
    if utils.config.get_option(config, "Cleanup", "unlaunch") == "true":
        unlaunch(sd_root)


def memory_pit(sd_root):
    print(" removing Memory Pit binary from SD card...")
    pit_filepath = utils.path.join(sd_root, "private/ds/app/484E494A/pit.bin")
    utils.file.remove_file(pit_filepath)


def flipnote_lenny(sd_root):
    region = utils.config.get_flipnote_lenny_region(config)
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
            region_path = utils.path.join(sd_root, path)
            utils.file.remove_directory(region_path)

    print(" removing Flipnote Lenny PPM files...")
    for file, path in files.items():
        directory_path = utils.path.join(sd_root, paths[region])
        filepath = utils.path.join(directory_path, path)
        utils.file.remove_file(filepath)


def unlaunch(sd_root):
    print(" removing Unlaunch files from SD card...")
    unlaunch_filepath = utils.path.join(sd_root, "UNLAUNCH.DSI")
    utils.file.remove_file(unlaunch_filepath)


def get_yes_no_input(prompt, default=True):
    while True:
        choice = input(prompt).strip().lower()

        if choice == "":
            return default
        elif choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("invalid choice: enter y or n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n:: Exiting...")

#!/usr/bin/env python3

# This bootstrap script follows this guide:
# https://dsi.cfw.guide/get-started.html

import utils

config = utils.get_config()
tmp_directory = "/tmp/dsi-bootstrap"


def main():
    print(
        ":: You should follow along with this guide: https://dsi.cfw.guide/get-started.html"
    )

    sd_root = utils.get_sd_root(config)

    print(" making temporary directory...")
    utils.make_directory(tmp_directory)

    print(":: Starting stage I")
    stage_1(sd_root)

    print(":: Starting stage II")
    stage_2(sd_root)

    print(":: Starting stage III")
    stage_3(sd_root)

    print(":: Cleaning up temporary files...")
    tmp_cleanup()

    print(":: Bootstrap complete!")


def stage_1(sd_root):
    if config["Bootstrap Stage I"]["twilight_menu"] == "True":
        print(" downloading TWiLight Menu++ ==> temp directory...")
        twilight_menu_url = "https://github.com/DS-Homebrew/TWiLightMenu/releases/latest/download/TWiLightMenu-DSi.7z"
        twilight_menu_filepath = utils.join_path(tmp_directory, "TWiLightMenu-DSi.7z")
        utils.download_url(twilight_menu_url, twilight_menu_filepath)

        print(" extracting TWiLight Menu++ 7-Zip archive...")
        utils.extract_7z(twilight_menu_filepath, tmp_directory)

        print(" moving TWiLight Menu++ files to SD card...")
        nds_path = utils.join_path(tmp_directory, "_nds")
        boot_nds_filepath = utils.join_path(tmp_directory, "BOOT.NDS")
        utils.copy_directory(nds_path, sd_root)
        utils.move_file(boot_nds_filepath, sd_root)

    if config["Bootstrap Stage I"]["dumptool"] == "True":
        print(" downloading dumpTool ==> SD card...")
        dump_tool_url = (
            "https://github.com/zoogie/dumpTool/releases/latest/download/dumpTool.nds"
        )
        dump_tool_filepath = utils.join_path(sd_root, "dumpTool.nds")
        utils.download_url(dump_tool_url, dump_tool_filepath)


def stage_2(sd_root):
    if config["Bootstrap Stage II"]["memory_pit"] == "True":
        memory_pit(sd_root)
    elif config["Bootstrap Stage II"]["flipnote_lenny"] == "True":
        flipnote_lenny(sd_root)


def memory_pit(sd_root):
    print(" making Nintendo DSi Camera directory...")
    camera_app_path = utils.join_path(sd_root, "private/ds/app/484E494A")
    utils.make_directory(camera_app_path)

    pit_url = ""
    pit_urls = {
        "facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/768_1024/pit.bin",
        "no_facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/256/pit.bin",
    }

    if config["Bootstrap Stage II"]["memory_pit_facebook_icon"] == "True":
        pit_url = pit_urls["facebook_icon"]
    elif config["Bootstrap Stage II"]["memory_pit_facebook_icon"] == "False":
        pit_url = pit_urls["no_facebook_icon"]
    else:
        print(":: Memory Pit Facebook Icon choice from config file is invalid")
        facebook_icon_choice = utils.get_yes_no_input(
            ">> Do you have a FaceBook icon (Y/n): "
        )

        if facebook_icon_choice:
            pit_url = pit_urls["facebook_icon"]
        else:
            pit_url = pit_urls["no_facebook_icon"]

    print(" downloading Memory Pit binary ==> SD card...")
    pit_filepath = utils.join_path(camera_app_path, "pit.bin")
    utils.download_url(pit_url, pit_filepath)


def flipnote_lenny(sd_root):
    print(" copying private directory to SD card...")
    script_directory = utils.get_script_directory()
    private_directory = utils.join_path(script_directory, "flipnote-lenny/private")
    utils.copy_directory(private_directory, sd_root)


def stage_3(sd_root):
    if config["Bootstrap Stage III"]["unlaunch"] == "True":
        unlaunch(sd_root)

    if config["Bootstrap Stage III"]["godmode9i"] == "True":
        godmode9i(sd_root)


def unlaunch(sd_root):
    print(" downloading Unlaunch ==> temp directory...")
    unlaunch_url = "https://problemkaputt.de/unlaunch.zip"
    unlaunch_zip_filepath = utils.join_path(tmp_directory, "unlaunch.zip")
    utils.download_url(unlaunch_url, unlaunch_zip_filepath)

    print(" extracting Unlaunch zip archive...")
    utils.extract_zip(unlaunch_zip_filepath, tmp_directory)

    print(" moving Unlaunch files to SD card...")
    unlaunch_filepath = utils.join_path(tmp_directory, "UNLAUNCH.DSI")
    utils.move_file(unlaunch_filepath, sd_root)


def godmode9i(sd_root):
    print(" downloading GodMode9i ==> SD card...")
    godmode9i_url = "https://github.com/DS-Homebrew/GodMode9i/releases/latest/download/GodMode9i.nds"
    godmode9i_filepath = utils.join_path(sd_root, "GodMode9i.nds")
    utils.download_url(godmode9i_url, godmode9i_filepath)


def tmp_cleanup():
    if utils.path_exists(tmp_directory):
        utils.remove_directory(tmp_directory)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n:: Exiting...")
        exit(0)

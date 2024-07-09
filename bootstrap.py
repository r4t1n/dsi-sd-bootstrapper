#!/usr/bin/env python3

# This bootstrap script follows this guide:
# https://dsi.cfw.guide/get-started.html

import utils

class ConfigError(Exception):
    pass

config = ""
try:
    config = utils.get_config()
except ConfigError as e:
    print(e)
    exit(1)

tmp_directory = "/tmp/dsi-bootstrap"


def main():
    print(
        ":: You should follow along with this guide: https://dsi.cfw.guide/get-started.html"
    )

    sd_root = ""
    try:
        sd_root = utils.get_sd_root(config)
    except ConfigError as e:
        print(e)
        exit(1)

    sd_root_choice = utils.get_yes_no_input(
        f">> Is the following SD root path correct: {sd_root} (Y/n): "
    )

    if not sd_root_choice:
        print(":: Exiting...")
        exit(0)

    print(" making temporary directory...")
    try:
        utils.make_directory(tmp_directory)
    except Exception as e:
        print(e)

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
    if config["Bootstrap"]["TwilightMenu"] == "True":
        print(" downloading TWiLight Menu++ ==> temp directory...")
        twilight_menu_url = "https://github.com/DS-Homebrew/TWiLightMenu/releases/latest/download/TWiLightMenu-DSi.7z"
        twilight_menu_filepath = utils.join_path(tmp_directory, "TWiLightMenu-DSi.7z")
        try:
            utils.download_url(twilight_menu_url, twilight_menu_filepath)
        except Exception as e:
            print(e)

        print(" extracting TWiLight Menu++ 7-Zip archive...")
        try:
            utils.extract_7z(twilight_menu_filepath, tmp_directory)
        except Exception as e:
            print(e)

        print(" moving TWiLight Menu++ files to SD card...")
        nds_path = utils.join_path(tmp_directory, "_nds")
        boot_nds_filepath = utils.join_path(tmp_directory, "BOOT.NDS")
        try:
            utils.copy_directory(nds_path, sd_root)
        except Exception as e:
            print(e)
        try:
            utils.move_file(boot_nds_filepath, sd_root)
        except Exception as e:
            print(e)

    if config["Bootstrap"]["DumpTool"] == "True":
        print(" downloading dumpTool ==> SD card...")
        dump_tool_url = (
            "https://github.com/zoogie/dumpTool/releases/latest/download/dumpTool.nds"
        )
        dump_tool_filepath = utils.join_path(sd_root, "dumpTool.nds")
        try:
            utils.download_url(dump_tool_url, dump_tool_filepath)
        except Exception as e:
            print(e)


def stage_2(sd_root):
    if config["Bootstrap"]["MemoryPit"] == "True":
        memory_pit(sd_root)
    elif config["Bootstrap"]["FlipnoteLenny"] == "True":
        flipnote_lenny(sd_root)


def memory_pit(sd_root):
    print(" making Nintendo DSi Camera directory...")
    camera_app_path = utils.join_path(sd_root, "private/ds/app/484E494A")
    try:
        utils.make_directory(camera_app_path)
    except Exception as e:
        print(e)

    pit_urls = {
        "facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/768_1024/pit.bin",
        "no_facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/256/pit.bin",
    }

    pit_url = ""
    if config["Bootstrap"]["MemoryPitFacebookIcon"] == "True":
        pit_url = pit_urls["facebook_icon"]
    elif config["Bootstrap"]["MemoryPitFacebookIcon"] == "False":
        pit_url = pit_urls["no_facebook_icon"]
    else:
        print("Error: Memory Pit Facebook Icon choice from config file is invalid")
        facebook_icon_choice = utils.get_yes_no_input(
            ">> Do you have a FaceBook icon (Y/n): "
        )

        if facebook_icon_choice:
            pit_url = pit_urls["facebook_icon"]
        else:
            pit_url = pit_urls["no_facebook_icon"]

    print(" downloading Memory Pit binary ==> SD card...")
    pit_filepath = utils.join_path(camera_app_path, "pit.bin")
    try:
        utils.download_url(pit_url, pit_filepath)
    except Exception as e:
        print(e)


def flipnote_lenny(sd_root):
    print(" copying private directory to SD card...")
    script_directory = utils.get_script_directory()
    private_directory = utils.join_path(script_directory, "flipnote-lenny/private")
    try:
        utils.copy_directory(private_directory, sd_root)
    except Exception as e:
        print(e)


def stage_3(sd_root):
    if config["Bootstrap"]["Unlaunch"] == "True":
        unlaunch(sd_root)

    if config["Bootstrap"]["Godmode9i"] == "True":
        godmode9i(sd_root)


def unlaunch(sd_root):
    print(" downloading Unlaunch ==> temp directory...")
    unlaunch_url = "https://problemkaputt.de/unlaunch.zip"
    unlaunch_zip_filepath = utils.join_path(tmp_directory, "unlaunch.zip")
    try:
        utils.download_url(unlaunch_url, unlaunch_zip_filepath)
    except Exception as e:
        print(e)

    print(" extracting Unlaunch zip archive...")
    try:
        utils.extract_zip(unlaunch_zip_filepath, tmp_directory)
    except Exception as e:
        print(e)

    print(" moving Unlaunch files to SD card...")
    unlaunch_filepath = utils.join_path(tmp_directory, "UNLAUNCH.DSI")
    try:
        utils.move_file(unlaunch_filepath, sd_root)
    except Exception as e:
        print(e)


def godmode9i(sd_root):
    print(" downloading GodMode9i ==> SD card...")
    godmode9i_url = "https://github.com/DS-Homebrew/GodMode9i/releases/latest/download/GodMode9i.nds"
    godmode9i_filepath = utils.join_path(sd_root, "GodMode9i.nds")
    try:
        utils.download_url(godmode9i_url, godmode9i_filepath)
    except Exception as e:
        print(e)


def tmp_cleanup():
    if utils.path_exists(tmp_directory):
        try:
            utils.remove_directory(tmp_directory)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n:: Exiting...")
        exit(0)

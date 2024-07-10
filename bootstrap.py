#!/usr/bin/env python3

import utils

config = utils.config.get_config()
tmp_directory = "/tmp/dsi-bootstrap"


def main():
    print(
        f"{utils.Color.start} {utils.Color.make_bold("Please follow along with this guide")}: https://dsi.cfw.guide/get-started.html"
    )

    sd_root = utils.config.get_sd_root(config)
    print(f"{utils.Color.start} {utils.Color.make_bold("SD root path")}: {sd_root}")

    sd_root_choice = get_yes_no_input(
        f"{utils.Color.start} {utils.Color.make_bold("Is the SD root path correct? [Y/n]")} "
    )

    if not sd_root_choice:
        exit()

    print(" making temporary directory...")
    utils.file.make_directory(tmp_directory)

    print(f"{utils.Color.start} {utils.Color.make_bold("Starting stage I...")}")
    stage_1(sd_root)

    print(f"{utils.Color.start} {utils.Color.make_bold("Starting stage II...")}")
    stage_2(sd_root)

    print(f"{utils.Color.start} {utils.Color.make_bold("Starting stage III...")}")
    stage_3(sd_root)

    print(
        f"{utils.Color.start} {utils.Color.make_bold("Cleaning up temporary files...")}"
    )
    tmp_cleanup()

    print(f"{utils.Color.start} {utils.Color.make_bold("Bootstrap complete!")}")


def stage_1(sd_root):
    if utils.config.get_option(config, "Bootstrap", "twilightMenu") == "true":
        print(" downloading TWiLight Menu++ ==> temp directory...")
        twilight_menu_url = "https://github.com/DS-Homebrew/TWiLightMenu/releases/latest/download/TWiLightMenu-DSi.7z"
        twilight_menu_filepath = utils.path.join(tmp_directory, "TWiLightMenu-DSi.7z")
        utils.network.download_url(twilight_menu_url, twilight_menu_filepath)

        print(" extracting TWiLight Menu++ 7-Zip archive...")
        utils.file.extract_7z(twilight_menu_filepath, tmp_directory)

        print(" moving TWiLight Menu++ files to SD card...")
        nds_path = utils.path.join(tmp_directory, "_nds")
        boot_nds_filepath = utils.path.join(tmp_directory, "BOOT.NDS")
        utils.file.copy_directory(nds_path, sd_root)
        utils.file.move_file(boot_nds_filepath, sd_root)

    if utils.config.get_option(config, "Bootstrap", "dumpTool") == "true":
        print(" downloading dumpTool ==> SD card...")
        dump_tool_url = (
            "https://github.com/zoogie/dumpTool/releases/latest/download/dumpTool.nds"
        )
        dump_tool_filepath = utils.path.join(sd_root, "dumpTool.nds")
        utils.network.download_url(dump_tool_url, dump_tool_filepath)


def stage_2(sd_root):
    if utils.config.get_option(config, "Bootstrap", "memoryPit") == "true":
        memory_pit(sd_root)
    elif utils.config.get_option(config, "Bootstrap", "flipnoteLenny") == "true":
        flipnote_lenny(sd_root)


def memory_pit(sd_root):
    print(" making Nintendo DSi Camera directory...")
    camera_app_path = utils.path.join(sd_root, "private/ds/app/484E494A")
    utils.file.make_directory(camera_app_path)

    print(" downloading Memory Pit binary ==> SD card...")
    pit_url = utils.config.get_memory_pit_url(config)
    pit_filepath = utils.path.join(camera_app_path, "pit.bin")
    utils.network.download_url(pit_url, pit_filepath)


def flipnote_lenny(sd_root):
    print(" copying private directory to SD card...")
    script_directory = utils.path.get_script_directory()
    private_directory = utils.path.join(script_directory, "flipnote-lenny/private")
    utils.file.copy_directory(private_directory, sd_root)


def stage_3(sd_root):
    if utils.config.get_option(config, "Bootstrap", "unlaunch") == "true":
        unlaunch(sd_root)

    if utils.config.get_option(config, "Bootstrap", "godmode9i") == "true":
        godmode9i(sd_root)


def unlaunch(sd_root):
    print(" downloading Unlaunch ==> temp directory...")
    unlaunch_url = "https://problemkaputt.de/unlaunch.zip"
    unlaunch_zip_filepath = utils.path.join(tmp_directory, "unlaunch.zip")
    utils.network.download_url(unlaunch_url, unlaunch_zip_filepath)

    print(" extracting Unlaunch zip archive...")
    utils.file.extract_zip(unlaunch_zip_filepath, tmp_directory)

    print(" moving Unlaunch files to SD card...")
    unlaunch_filepath = utils.path.join(tmp_directory, "UNLAUNCH.DSI")
    utils.file.move_file(unlaunch_filepath, sd_root)


def godmode9i(sd_root):
    print(" downloading GodMode9i ==> SD card...")
    godmode9i_url = "https://github.com/DS-Homebrew/GodMode9i/releases/latest/download/GodMode9i.nds"
    godmode9i_filepath = utils.path.join(sd_root, "GodMode9i.nds")
    utils.network.download_url(godmode9i_url, godmode9i_filepath)


def tmp_cleanup():
    if utils.path.exists(tmp_directory):
        utils.file.remove_directory(tmp_directory)


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
        exit()

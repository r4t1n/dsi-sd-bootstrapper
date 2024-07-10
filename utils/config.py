import configparser
import utils


def get_config():
    config_filepath = utils.path.join(
        utils.path.get_script_directory(), "../config.ini"
    )

    if not utils.path.exists(config_filepath):
        print(
            f"{utils.Color.make_red("error reading config file")}: '{config_filepath}' does not exist"
        )
        exit(1)

    config = configparser.ConfigParser()

    try:
        config.read(config_filepath)
    except configparser.Error as config_error:
        print(f"{utils.Color.make_red("error reading config file")}: {config_error}")
        exit(1)

    return config


def get_option(config, section, option):
    try:
        return config.get(section, option)
    except (configparser.NoSectionError, configparser.NoOptionError) as config_error:
        print(f"{utils.Color.make_red("error getting config option")}: {config_error}")
        exit(1)


def get_sd_root(config):
    sd_root = get_option(config, "Options", "sdRoot")

    if not utils.path.exists(sd_root):
        print(
            f"{utils.Color.make_red("error getting SD root")}: 'sdRoot' from config is invalid"
        )
        exit(1)

    return sd_root


def get_memory_pit_url(config):
    pit_urls = {
        "facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/768_1024/pit.bin",
        "no_facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/256/pit.bin",
    }

    memory_pit_facebook_icon = get_option(config, "Bootstrap", "memoryPitFacebookIcon")
    pit_url = ""

    if memory_pit_facebook_icon == "true":
        pit_url = pit_urls["facebook_icon"]
    elif memory_pit_facebook_icon == "false":
        pit_url = pit_urls["no_facebook_icon"]
    else:
        print(
            f"{utils.Color.make_red("error getting Memory Pit Facebook icon")}: 'memoryPitFacebookIcon' from config is invalid"
        )
        exit(1)

    return pit_url


def get_flipnote_lenny_region(config):
    region = get_option(config, "Bootstrap", "flipnoteLennyRegion")
    regions = {"Japan": 1, "USA": 2, "Europe/Australia": 3}

    if region not in regions:
        print(
            f"{utils.Color.make_red("error getting Flipnote Lenny region")}: 'flipnoteLennyRegion' from config is invalid"
        )
        exit(1)

    return regions[region]

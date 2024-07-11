import tomllib
import utils


def get_config():
    config_filepath = utils.path.join(utils.path.script_directory(), "../config.toml")
    try:
        with open(config_filepath, mode="rb") as config_file:
            return tomllib.load(config_file)
    except FileNotFoundError as file_error:
        print(utils.Color.format_error(file_error))
        exit(1)


def value(config, table, key):
    try:
        return config[table][key]
    except KeyError:
        print(utils.Color.format_error(f"'{key}' from config.toml is invalid"))
        exit(1)
    except Exception as error:
        print(utils.Color.format_error(error))
        exit(1)


def get_sd_root(config):
    sd_root = value(config, "options", "sd_root")

    if not utils.path.exists(sd_root):
        print(utils.Color.format_error("'sd_root' from config.toml is invalid"))
        exit(1)

    return sd_root


def get_memory_pit_url(config):
    pit_urls = {
        "facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/768_1024/pit.bin",
        "no_facebook_icon": "https://dsi.cfw.guide/assets/files/memory_pit/256/pit.bin",
    }
    memory_pit_facebook_icon = value(config, "bootstrap", "memory_pit_facebook_icon")

    if memory_pit_facebook_icon:
        return pit_urls["facebook_icon"]
    elif not memory_pit_facebook_icon:
        return pit_urls["no_facebook_icon"]
    else:
        print(utils.Color.format_error("'memory_pit_facebook_icon' from config.toml is invalid"))
        exit(1)


def get_flipnote_lenny_region(config):
    region = value(config, "bootstrap", "flipnote_lenny_region")
    regions = {"Japan": 1, "USA": 2, "Europe/Australia": 3}

    if region not in regions:
        print(utils.Color.format_error("'flipnote_lenny_region' from config.toml is invalid"))
        exit(1)

    return regions[region]

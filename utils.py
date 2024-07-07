import configparser
import os
import shutil
import subprocess
import urllib.error
import urllib.request


def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))


def get_config():
    config_filepath = join_path(get_script_directory(), "config.ini")

    if not path_exists("config.ini"):
        print(f"Error: config file {config_filepath} does not exist")
        exit(1)

    config = configparser.ConfigParser()

    try:
        config.read(config_filepath)
    except configparser.Error as error:
        print(f"Error reading config file: {error}")

    return config

def get_sd_root(config):
    sd_root = config["Settings"]["sd_root"]

    if sd_root == "":
        print(":: SD root path from config file is empty, please edit config.ini")
        exit(1)
    elif check_valid_path(sd_root):
        print(f":: Using following SD root path from config file: {sd_root}")
        sd_root_choice = get_yes_no_input(
            ">> Is the following SD root path correct (Y/n): "
        )

        if not sd_root_choice:
            print(":: Exiting...")
            exit(0)

        return sd_root
    else:
        print(":: Invalid SD root path in config file, please edit config.ini")
        exit(1)


def get_flipnote_lenny_region(config):
    region = config["Cleanup"]["flipnote_lenny_region"]
    regions = {"Japan": 1, "USA": 2, "Europe/Australia": 3}

    if region == "":
        print(
            ":: Flipnote Lenny region from config file is empty, please edit config.ini"
        )
        exit(1)
    elif region in regions:
        print(f":: Using the following region: {region}")
        return regions[region]
    else:
        print(":: Invalid region in config file, please edit config.ini")


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
            print("Invalid choice, enter y or n")


def join_path(path, *paths):
    return os.path.join(path, *paths)


def path_exists(path):
    return os.path.exists(path)


def check_valid_path(path):
    if os.path.exists(path):
        return True
    else:
        print(f"Error: {path} does not exist")
        return False


def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f" made directory: {path}")
    except OSError as error:
        print(f"Error creating directory {path}: {error}")


def remove_directory(path):
    try:
        shutil.rmtree(path)
        print(f" removed directory: {path}")
    except FileNotFoundError:
        print(f"Error: {path} not found")
    except PermissionError:
        print(f"Error: Permission denied for {path}")
    except Exception as error:
        print(f"Error: {error}")


def remove_file(path):
    try:
        os.remove(path)
        print(f" removed file: {path}")
    except FileNotFoundError:
        print(f"Error: {path} not found")
    except PermissionError:
        print(f"Error: Permission denied for {path}")
    except Exception as error:
        print(f"Error: {error}")


def download_url(url, filepath):
    headers = {"User-Agent": "Python urllib"}
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response, open(
            filepath, "wb"
        ) as output:
            data = response.read()
            output.write(data)
        print(f" downloaded file: {filepath}")
    except urllib.error.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except urllib.error.URLError as url_error:
        print(f"URL error occurred: {url_error}")
    except Exception as error:
        print(f"An error occurred: {error}")


def extract_7z(filepath, output_path):
    try:
        subprocess.run(
            ["7z", "x", filepath, f"-o{output_path}", "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
        print(f" extracted 7-Zip archive: {filepath}")
    except subprocess.CalledProcessError as error:
        print(f"Error extracting {filepath}: {error}")


def extract_zip(filepath, output_path):
    try:
        subprocess.run(
            ["unzip", filepath, "-d", output_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
        print(f" extracted zip archive: {output_path}")
    except subprocess.CalledProcessError as error:
        print(f"Error extracting {filepath}: {error}")


def move_file(source, destination):
    try:
        if os.path.isfile(source):
            shutil.move(source, destination)
            print(f" moved file {source} to {destination}")
        else:
            print(f"Error moving file: {source} is not a file")
    except FileNotFoundError:
        print(f"Error moving file: {source} not found")
    except PermissionError:
        print(f"Error moving file: Permission denied for {destination}")
    except Exception as error:
        print(f"Error moving file: {error}")


def copy_directory(source, destination):
    try:
        if os.path.isdir(source):
            destination = os.path.join(destination, os.path.basename(source))
            make_directory(destination)
            shutil.copytree(source, destination, dirs_exist_ok=True)
            print(f" copied directory {source} to {destination}")
        else:
            print(f"Error moving directory: {source} is not a directory")
    except FileNotFoundError:
        print(f"Error: {source} not found")
    except PermissionError:
        print(f"Error: Permission denied for {destination}")
    except Exception as error:
        print(f"Error: {error}")

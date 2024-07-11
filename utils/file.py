import os
import shutil
import subprocess
import utils


def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as os_error:
        print(utils.Color.format_error(os_error))
        exit(1)


def remove_directory(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError as file_error:
        print(utils.Color.format_error(file_error))
    except PermissionError as permission_error:
        print(utils.Color.format_error(permission_error))
    except Exception as error:
        print(utils.Color.format_error(error))


def remove_file(path):
    try:
        os.remove(path)
    except FileNotFoundError as file_error:
        print(utils.Color.format_error(file_error))
    except PermissionError as permission_error:
        print(utils.Color.format_error(permission_error))
    except Exception as error:
        print(utils.Color.format_error(error))


def extract_7z(filepath, output):
    try:
        subprocess.run(
            ["7z", "x", filepath, f"-o{output}", "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError as error:
        print(utils.Color.format_error(error))
        exit(1)


def extract_zip(filepath, output):
    try:
        subprocess.run(
            ["unzip", filepath, "-d", output],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError as error:
        print(utils.Color.format_error(error))
        exit(1)


def move(source, destination):
    try:
        shutil.move(source, destination)
    except FileNotFoundError as file_error:
        print(utils.Color.format_error(file_error))
    except PermissionError as permission_error:
        print(utils.Color.format_error(permission_error))
    except Exception as error:
        print(utils.Color.format_error(error))

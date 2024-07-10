import os
import shutil
import subprocess
import utils


def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f" made directory: {path}")
    except OSError as os_error:
        print(f"{utils.Color.make_red("error making directory")}: {os_error}")
        exit(1)


def remove_directory(path):
    try:
        shutil.rmtree(path)
        print(f" removed directory: {path}")
    except FileNotFoundError as file_error:
        print(f"{utils.Color.make_red("error removing directory")}: {file_error}")
    except PermissionError as permission_error:
        print(f"{utils.Color.make_red("error removing directory")}: {permission_error}")
    except Exception as error:
        print(f"{utils.Color.make_red("error removing directory")}: {error}")


def remove_file(path):
    try:
        os.remove(path)
        print(f" removed file: {path}")
    except FileNotFoundError as file_error:
        print(f"{utils.Color.make_red("error removing file")}: {file_error}")
    except PermissionError as permission_error:
        print(f"{utils.Color.make_red("error removing file")}: {permission_error}")
    except Exception as error:
        print(f"{utils.Color.make_red("error removing file")}: {error}")


def extract_7z(filepath, output):
    try:
        subprocess.run(
            ["7z", "x", filepath, f"-o{output}", "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
        print(f" extracted 7-Zip archive: {filepath}")
    except subprocess.CalledProcessError as error:
        print(f"{utils.Color.make_red("error extracting 7-Zip archive")}: {error}")
        exit(1)


def extract_zip(filepath, output):
    try:
        subprocess.run(
            ["unzip", filepath, "-d", output],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
        print(f" extracted zip archive: {filepath}")
    except subprocess.CalledProcessError as error:
        print(f"{utils.Color.make_red("error extracting zip archive")}: {error}")
        exit(1)


def move_file(source, destination):
    try:
        if os.path.isfile(source):
            shutil.move(source, destination)
            print(f" moved file {source} to {destination}")
        else:
            print(
                f"{utils.Color.make_red("error moving file")}: '{source}' is not a file"
            )
    except FileNotFoundError as file_error:
        print(f"{utils.Color.make_red("error moving file")}: {file_error}")
    except PermissionError as permission_error:
        print(f"{utils.Color.make_red("error moving file")}: {permission_error}")
    except Exception as error:
        print(f"{utils.Color.make_red("error moving file")}: {error}")


def copy_directory(source, destination):
    try:
        if os.path.isdir(source):
            destination = utils.path.join(destination, os.path.basename(source))
            shutil.copytree(source, destination)
            print(f" copied directory {source} to {destination}")
        else:
            print(
                f"{utils.Color.make_red("error copying directory")}: '{source}' is not a directory"
            )
    except FileNotFoundError as file_error:
        print(f"{utils.Color.make_red("error copying directory")}: {file_error}")
    except PermissionError as permission_error:
        print(f"{utils.Color.make_red("error copying directory")}: {permission_error}")
    except Exception as error:
        print(f"{utils.Color.make_red("error copying directory")}: {error}")

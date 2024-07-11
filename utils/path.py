import os
import pathlib


def to_path(path):
    return pathlib.Path(path)


def script_directory():
    return pathlib.Path(__file__).resolve().parent


def join(*paths):
    return pathlib.Path(*paths)


def exists(path):
    return os.path.exists(path)

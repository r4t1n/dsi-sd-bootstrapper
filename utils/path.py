import os


def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))


def join(path, *paths):
    return os.path.join(path, *paths)


def exists(path):
    return os.path.exists(path)

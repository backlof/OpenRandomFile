import os


# Get relative path from current folder (script location)
def get_relative_path(folder):
    absolute_path = folder
    try:
        relative_path = os.path.relpath(absolute_path, get_current_dir())
        return relative_path
    except ValueError:
        # Folder is on a different drive
        return absolute_path


# Get the current directory
def get_current_dir():
    directory, script = os.path.split(os.path.realpath(__file__))
    return directory
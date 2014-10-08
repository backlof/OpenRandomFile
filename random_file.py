#! /usr/bin/python3

import os
import json
import random
import sys

data_file = 'folders.json'


def get_files(folders, extensions=[]):
    files = []

    for folder in folders:
        for root, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith(tuple(extensions)):
                    files.append(os.path.join(root,filename))

    return files


def get_random(folders, extensions=[]):
    files = get_files(folders, extensions)

    if files:
        return random.choice(files)
    else:
        print('No files found.')
        sys.exit(0)


# Get relative path from current folder (script location)
def get_relative_path(folder):
    absolute_path = folder
    # Separates filename out of absolute path to script
    current_dir, script = os.path.split(os.path.realpath(__file__))

    try:
        relative_path = os.path.relpath(absolute_path, current_dir)
        return relative_path
    except ValueError:
        # Folder is on a different drive
        return absolute_path


def default_dictionary():
    folders = []
    extensions = ['.py', '.txt']
    dictionary = {'folders': folders, 'file_extensions': extensions}
    return dictionary


def load_data():
    if os.path.isfile(data_file):
        content = open(data_file).read()
        return json.loads(content)
    else:
        return default_dictionary()


def write_data(dictionary):
    with open(data_file, 'w+') as outfile:
        json.dump(dictionary, outfile, indent=4)


def run_file(path):
    import subprocess

    # Windows
    if os.name == 'nt':
        os.system('start ' + '"' + path + '"')
    # Mac OS X
    elif sys.platform.startswith('darwin'):
        subprocess.call(('open', path))
    # Linux
    elif os.name == 'posix':
        subprocess.call(('xdg-open', path))


if __name__ == "__main__":
    settings = load_data()

    if not settings["folders"]:
        print('You need to add a folder first.')
    else:
        file = get_random(settings["folders"], settings["file_extensions"])
        print(file)
        run_file(file)

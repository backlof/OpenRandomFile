#! /usr/bin/env python

import os
import json
import random
import sys

data_file = 'folders.json'


def get_files(folders, extensions=[], exclude=[]):
    files = []

    # Exclude not implemented

    for folder in folders:
        for root, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                if filename.lower().endswith(tuple(extensions)):
                    print(filename)
                    files.append(os.path.join(root,filename))

    return files


def get_random(folders, extensions=[], exclude=[]):
    files = get_files(folders, extensions)

    if files:
        return random.choice(files)
    else:
        print('No files found.')
        sys.exit(0)


def default_dictionary():
    folders = []
    extensions = ['.mkv', '.wmv', '.avi', '.mpg', '.mpeg', '.flv', '.mov']
    exclude = ['sample']
    dictionary = {'folders': folders, 'file_extensions': extensions, 'exclude_names': exclude}
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
        os.startfile(path, 'open')
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
        file = get_random(settings["folders"], settings["file_extensions"], settings["exclude_names"])
        print(file)
        run_file(file)
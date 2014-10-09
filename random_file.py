#! /usr/bin/env python

import os
import json
import random
import sys

name = 'settings'
data_file = name + '.json'
json_dirs = 'directories'
json_ext = 'file_extensions'
json_excl = 'exclude_term'
json_size = 'minimum_size_byte'


def get_files(folders, extensions=[], exclude=[], minimum=0):
    files = []

    # Exclude not implemented

    for folder in folders:
        for root, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                absolute_path = os.path.join(root,filename)
                if filename.lower().endswith(tuple(extensions)) and os.stat(absolute_path).st_size > minimum:
                    files.append(absolute_path)

    return files


def get_random(folders, extensions=[], exclude=[], minimum=0):
    files = get_files(folders, extensions, exclude, minimum)

    if files:
        return random.choice(files)
    else:
        print('No files found.')
        sys.exit(0)


def default_dictionary():
    folders = []
    extensions = ['.mkv', '.wmv', '.avi', '.mpg', '.mpeg', '.flv', '.mov']
    exclude = []
    minimum = 104857600
    dictionary = {json_dirs: folders, json_ext: extensions, json_excl: exclude, json_size: minimum}
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

    if not settings[json_dirs]:
        print('You need to add a folder first.')
    else:
        file = get_random(settings[json_dirs], settings[json_ext], settings[json_excl])
        run_file(file)
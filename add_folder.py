#! /usr/bin/env python

import random_file
import path_tools

if __name__ == "__main__":
    settings = random_file.load_data()

    try:
        from tkinter import filedialog
        filedialog.Tk().withdraw()
        directory = filedialog.askdirectory()
        relative_path = path_tools.get_relative_path(directory)

        if not relative_path in settings[random_file.json_dirs]:
            settings[random_file.json_dirs].append(relative_path)
        else:
            print('Directory was already in the list.')
    except ImportError:
        print('No tkinter support. Change the contents of folder.json manually.')

        relative_path = path_tools.get_relative_path(path_tools.get_current_dir())

        if not relative_path in settings[random_file.json_dirs]:
            print('Adding this directory...')
            settings[random_file.json_dirs].append(relative_path)

    random_file.write_data(settings)
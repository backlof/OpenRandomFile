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

        if not relative_path in settings['folders']:
            settings['folders'].append(relative_path)
        else:
            print('Folder was already in the list.')
    except ImportError:
        print('No tkinter support. Change the contents of folder.json manually.')

        relative_path = path_tools.get_relative_path(path_tools.get_current_dir())

        if not relative_path in settings['folders']:
            print('Adding this folder...')
            settings['folders'].append(relative_path)

    random_file.write_data(settings)
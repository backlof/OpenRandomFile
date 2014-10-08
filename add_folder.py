#! /usr/bin/python3

import random_file


def prompt_dir():
	try:
		from tkinter import filedialog
		filedialog.Tk().withdraw()
		directory = filedialog.askdirectory()
		return directory
	except ImportError:
		while True:
			folder = input('Enter a directory: ')
			if os.path.exists(folder):
				return folder


if __name__ == "__main__":
    settings = random_file.load_data()

    folder = prompt_dir()
    relative_path = random_file.get_relative_path(folder)
    settings['folders'].append(relative_path)
    random_file.write_data(settings)

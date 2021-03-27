from distutils.dir_util import copy_tree
from datetime import datetime
import os


def main():
    width = 80

    print(width * "=")
    print('backup'.center(width, ' '))
    print(width * "-")
    now = str(datetime.now().date()).replace('-', '_')
    print(f"creating backup directory at time: '{now}'..")

    path = f'backup/{now}'

    if not os.path.isdir(path):
        os.mkdir(path)
        print(f'Created {path} ! ..')
    else:
        print("Folder already exists. therefore continuing..")

    # copy to backup folder
    print('Copying files from automate folder to backup folder...')
    from_directory = "automate"
    to_directory = path

    copy_tree(from_directory, to_directory)

    print(width * "-")
    print("Backup successful".center(width, ' '))
    print(width * "*")


if __name__ == "__main__":
    main()

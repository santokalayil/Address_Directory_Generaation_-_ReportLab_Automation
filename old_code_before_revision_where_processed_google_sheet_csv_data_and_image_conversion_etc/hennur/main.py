import os
from subprocess import call
import platform
import sys

# importing my python script as module
from csv_files import copy_original
from image.convert import convert_images
from data.preprocess import preprocess
from database import dataframe_to_sqlite
from database import post_process


class CallPyScript:
    def __init__(self, file_url):

        # Dealing platform issues of slashes while accessing files inside folder
        if platform.system() == "Windows":
            file_url = file_url
        else:
            if '\\' in file_url:
                file_url = file_url.replace("\\", "/")

        # Dealing platform issues of python version 3
        self.python = "python" if platform.system() == "Windows" else "python3" \
            if platform.system() == "Linux" else sys.exit(1)

        self.file_url = file_url
        self.file_url = self.get_path()

    def get_path(self):
        path = os.getcwd()
        file_url = os.path.join(path, self.file_url)
        return file_url

    def run(self):
        call([self.python, self.file_url])


def run_scripts():
    # Dealing platform issues while printing python version information
    if platform.system() == "Windows":
        call(["python", "--version"])  # python version checking
    elif platform.system() == "Linux":
        call(["python3", "--version"])
    else:
        print("Operating System is not supported!")
        sys.exit(1)

    # # PRE-PROCESS
    # copy_original.run()  # running csv_files copying script function from my own script
    # preprocess()  # preprocess data
    # dataframe_to_sqlite()  # storing in sqlite database
    # data_script = CallPyScript(os.path.join("data", "__init__.py"))  # running data_script
    # data_script.run()
    #
    # # convert images to smaller format
    # convert_images()
    #
    # POST-PROCESS
    # post process injection of data into sqlite database -- AFTER MANUAL EDIT BY ALEX
    # post_process.process()

    # from database.edit import run_updates  # code based manual data editing - automation
    # run_updates()
    from pdf_generation import render
    render()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_scripts()

#
# Example file for working with o.s path module


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():


    # Get the modification time
    t = time.ctime(path.getmtime("demo.txt.bak"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("demo.txt.bak")))


if __name__ == "__main__":
    main()
import os
import shutil
from os import path

def main():
# make a duplicate of an existing file
    if path.exists("Python.txt"):
    # get the path to the file in the current directory
     src = path.realpath("Python.txt");

    # rename the original file
    os.rename('demo.txt', 'demo.txt')

if __name__ == "__main__":
    main()

import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
# Check if file exists
    if path.exists("demo.txt"):
# get the path to the file in the current directory
        src = path.realpath("demo.txt");
# rename the original file
    #os.rename("career.demo.txt","demo.txt")
# now put things into a ZIP archive
    root_dir,tail = path.split(src)
    shutil.make_archive("demo archive", "zip", root_dir)
# more fine-grained control over ZIP files
    with ZipFile("testdemo.zip","w") as newzip:
        newzip.write("demo.txt")
    newzip.write("demo.txt.bak")
if __name__== "__main__":
      main()



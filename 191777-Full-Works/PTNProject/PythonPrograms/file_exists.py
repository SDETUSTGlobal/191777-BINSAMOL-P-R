import os.path
from os import path
def main():

   print ("File exists:"+str(path.exists('demo.txt')))
   print ("File exists:" + str(path.exists('career.Python.txt')))
   print ("directory exists:" + str(path.exists('PythonPrograms')))

if __name__== "__main__":
   main()

os.path.isfile()
import os.path
from os import path
def main():

	print ("Is it File?" + str(path.isfile('demo.txt')))
	print ("Is it File?" + str(path.isfile('PythonPrograms')))
if __name__== "__main__":
	main()

#pathlibPath.exists() For Python 3.4
import pathlib

file = pathlib.Path("demo.txt")
if file.exists():
	print("File exist")
else:
	print("File not exist")



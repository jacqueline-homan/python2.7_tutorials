import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
# Make a copy or duplicate of an existing file
	if path.exists("textfile.txt"):
		# Get the path of the file in the current directory
		src = path.realpath("textfile.txt")
		# Separate the path part from the filename
		head, tail = path.split(src)
		print "path: " + head
		print "file: " + tail

		# Now, make a backup file
		dst = src + ".bak"
		# Then use the shell to make a copy of the file
		shutil.copy(src,dst)
		# If you want to copy over perms, modification times, and other datta
		shutil.copystat(src,dst)


	


if __name__ == "__main__":
	main()
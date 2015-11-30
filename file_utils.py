import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
 # Check if file exists
def main():
	print os.name;
	print "File exists: " + str(path.exists("textfile.txt"))
	print "File is a file: " + str(path.isfile("textfile.txt"))
	print "File is a directory: " + str(path.isdir("textfile.txt"))

	# Work with file paths
	print "File path: " + str(path.realpath("textfile.txt"))
	print "File path and name: " + str(path.split(path.realpath("textfile.txt")))

	# Get modification times
	t = time.ctime(path.getmtime("textfile.txt"))
	print t
	print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

	# Compute how long it's been since file has been modified
	td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "It's been " + str(td) + " since file was modified"
	print "Or, if you prefer, " + str(td.total_seconds()) + " seconds since it was modified (just sayin')"

if __name__ == "__main__":
	main()
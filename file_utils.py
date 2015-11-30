import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
 # Check if file exists
print os.name;
print "File exists: " + str(path.exists("textfile.txt"))
print "File is a file: " + str(path.isfile("textfile.txt"))
print "File is a directory: " + str(path.isdir("textfile.txt"))

# Work with file paths
print "File path: " + str(path.realpath("textfile.txt"))
print "File path and name: " + str(path.split(path.realpath("textfile.txt")))
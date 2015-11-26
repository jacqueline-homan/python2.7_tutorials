from datetime import date
from datetime import time
from datetime import datetime

def main():
	today = date.today()
	print "Today is ", today
	print " "
	print "Date Components: ", today.day, today.month, today.year
	print " "
	print "Today is weekday #: ", today.weekday()
	print " "
	today = datetime.now()
	print "The current date and time is: ", today;
	print " "
	t = datetime.time(datetime.now())
	print "The current time is: ", t
	print " "
	wd = date.weekday(today)
	print " "
	days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
	#print "Today is day number %d" % wd
	#print "which is a " + days[wd]
	print "Today is " + days[wd] + " which is the %d day of the week if we make Sunday day number 0" % wd
	print " "
	print "And now we'll do some datetime formatting :) "
	print " "
	now = datetime.now()
	print now.strftime("%Y")
	print " "
	print now.strftime("%a, %d %B, %Y")
	print " "
	print now.strftime("%c")
	print now.strftime("%x")
	print now.strftime("%X")
	print " "
	print now.strftime("%I:%M:%S %p")
	print now.strftime("%H:%M")

if __name__ == "__main__":
	main()
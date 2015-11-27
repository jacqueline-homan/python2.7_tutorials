from datetime import timedelta
from datetime import datetime
from datetime import date
from datetime import time

print "Construct a basic timedelta and print it out: "
print timedelta(days=365, hours=5, minutes=1)
print " "
print "Print today's date: "
print "Today is: " + str(datetime.now())
print " "
print "Print today's date a year and 2 weeks from now: "
print "A year from now will be: " + str(datetime.now() + timedelta(weeks=2))
print " "
print "2 weeks and 3 days from now: " + str(datetime.now() + timedelta(weeks=2, days=3))

# Computing the date one week ago, formatted as a string:
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print "One week ago, it was: " + s

# Computing the number of days until April Fools Day:
today = date.today() # get today's dat e
afd = date(today.year, 4, 1) # get April Fools for same year
# use date comparison if April Fools is already gone for this year
# and if so, use the replace() function to get it for next year
if afd < today:
	print "April Fools already went %d days ago" % ((today-afd).days)
	afd = afd.replace(year=today.year + 1) # getting next year's April Fools

# Now, compute the amount of days until next April Fools
time_to_afd = abs(afd - today)
print time_to_afd.days, "days until next April Fools Day!"
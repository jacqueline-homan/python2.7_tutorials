import calendar

# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2015, 11)
print str

# Create an HTML of a formatted calendar. NOTE: When you run this
# in your terminal, it outputs the equivalent of what you'd see
# if you ran the 'cat' <filename> command to inspect an HTML file
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2015, 1)
print str

# Loop over the days of a month
# Zeros mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2015, 11):
	print i

# The Calendar module provides utilities for the given locale,
# such as the names of the days and months in both full and
# abbreviated forms
for name in calendar.month_name:
	print name

for day in calendar.day_name:
	print day

# Compute days based on a rule. Consider a team meeting
# on the 1st Friday of every month. 
# Use this script to figure out what days
# that would be for each month:
for m in range(1, 13):
	# returns an array of weeks that represent the month
	cal = calendar.monthcalendar(2015, m)
	# The 1st Friday has to be within the first 2 weeks
	week1 = cal[0]
	week2 = cal[1]

	if week1[calendar.FRIDAY] != 0:
		meetday = week1[calendar.FRIDAY]
	else:
	# if 1st Friday isn't i the 1st week, it must be in the 2nd
		meetday = week2[calendar.FRIDAY]
	print "%10s %2d" % (calendar.month_name[m], meetday)
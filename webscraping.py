import urllib2
import json

def main():
	# Open a connection to a URL using urllib2
	webUrl = urllib2.urlopen("https://disqus.com")

	# Get the result code and print it
	print "result code: " + str(webUrl.getcode()) # HTTP result code ( 200 if no errors)

	# Read the data from the URL and print it
	data = webUrl.read()
	print data


if __name__ == "__main__":
	main()

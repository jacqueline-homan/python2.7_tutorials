def main():
# Open a file for writing and create it if it doesn't exist
	f = open("textfile.txt", "w+")
#Write 10 lines of text and the line numbers to the file
	for i in range(10):
		f.write("This is line  %d\n\r" % (i+1))
 #Open the file to append data to the end
	f = open("textfile.txt", "a+")
	for i in range(10):
		f.write("And this line %d\n\r" % (i+1))

# Close file when done
	f.close()

# Open the file back up for reading the contents
	f = open("textfile.txt", "r")
	if f.mode == 'r':
		contents = f.read()
		flines = f.readlines()
		for x in flines:
			print x

	f.close()



if __name__ == "__main__":
	main()
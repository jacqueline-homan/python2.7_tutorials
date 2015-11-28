def main():
	x = 0
	# Define while-loop:
	while (x < 5):
		print x
		x = x + 1

	# Define a for-loop:
	for x in range(15, 20):
		print x

	# Use a for-loop over a collection:
	recipes = ["fish", "soup", "salad", "beef", "chicken"]
	for r in recipes:
		print r

	# Using break and continue: Take turns commenting out the if-statements
	# and observe the results printed out
	for x in range(5, 10):
		if (x == 7): break
		if (x % 2 == 0): continue
		print x

    # Using Python's enumerate() function to return 
    # an index number for each item in the collection
    # along with the elements of that collection:
	recipes = ["fish", "soup", "salad", "beef", "chicken"]
	for i, r in enumerate(recipes):
		print i, r

	for x in range(2, 10):
		if x % 2 == 0:
			print "Even Steven!", x
			continue
		print "Odd man out!", x

if __name__ == "__main__":
	main()
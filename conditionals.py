# Program control flow - Conditionals
def main():
	x, y = 10, 100

	if(x < y):
		st= "x is less than y"
	elif (x == y):
		st= "x is the same as y"
	else:
		st= "x is greater than y"
	print st

# Python lets us condense if-else blocks if you use 
# "a if c else b", like so:

# st = "x is less then y" if(x < y) else "x is greater
#      than or  equal to y"

# So you can replace the entire if-else block above with
# a single line of code

# Calling the function main():
if __name__ == "__main__":
    main()
# This Python tutorial uses Python 2.7


#printing out the Fibonacci sequence vertically
a, b = 0, 1
while b < 10:
	print b
	a, b = b, a+b

# printing out the Fibonacci sequence horizontally
a, b = 0, 1
while b < 10:
	print b,
	a, b = b, a+b

#printing out from user input, dialogue w/ user
myName = raw_input("What is your name?")
print "OK, you said your name is:", (myName)

user_response = raw_input("Is this correct - Y or N ?")
print "You answered:",(user_response)


# defining a function for a Py web app
def main():
  print "hello ya nerd!"
 
if __name__ == "__main__":
	main()

print "Yup"

main()

# declaring and intializing a variable
f = 0;
print f

#re-declaring a variable
f = "do rei me"
print f
#converting to a string to avoid TypeError
print "do rei me" + str(123)

# local variable
def some_function():
	f = "blah blah blah"
	print f

some_function()
print f

#global variable
def some_function():
	global f
	f = "blah blah blah"
	print f

some_function()
print f

del f
print f



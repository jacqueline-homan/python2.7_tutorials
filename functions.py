# This Python tutorial uses Python 2.7

# define a function
def func1():
  print "I am a function"
# Here we call the function and it executes
func1() 

#print func1()
#print 

# A function that takes args (or parameters) but returns no value:
def func2(arg1, arg2):
  print arg1, " ", arg2

func2(10, "Your momma")
print func2("Hip to be", " square")

# Function that returns a value
def cube(x):
  return x*x*x

print cube(3)

# Function w/ default value for an arg:
def power(num, x=1):
  result = 1;
  for i in range(x):
  	result = result * num
  return result
print power(2)
print power(2, 3)
print power(x=3, num=2)
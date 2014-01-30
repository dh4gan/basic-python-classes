# Written by Duncan Forgan, 2/05/12
# Simple script to demonstrate files, functions and exceptions
# This script uses the standard IO that comes with Python
# Other modules contain their own IO methods, and are generally preferable
# See next exercise on objects


title='Files, Functions and Exceptions Code'
bar = '-------'

print title
print 4*bar
print ''


print 'Functions'
print 2*bar
print ''

# Let's start by defining some functions first

def factorial(n):
    "Computes the Factorial of n"  # This is a docstring (http://en.wikipedia.org/wiki/Docstring#Python)
    result = 1
    for i in range(n):
        result = result*(i+1)         
    return result

def fib2(n=10): 
    "Return a list containing the Fibonacci series up to n"
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result    
    
test1 = factorial(4)
print 'Factorial is ',test1
print 'What does Factorial do? ',factorial.__doc__

test2 = fib2(7)
test3 = fib2() # Note that the default value of n is used here

print 'First Fibonacci Sequence: ',test2
print 'Second Fibonacci Sequence: ',test3

print ''
print 'Files'
print bar
print ''

# Open a basic ASCII file for writing
text_file = open("myfile.txt", "r")

# The second argument determines what you're going to do with the file
# r - reading (file needs to exist)
# w - writing (file created if non-existent, contents overwritten)
# a - append to a file
# r+ - read and write to a file (file needs to exist)
# w+ - write and read (If file exists, contents overwritten)
# a+ - append and read

# Read the entire contents into a string

contents = text_file.read()

print 'Contents:  ', contents

# Or we can just read a few characters
# Close the file first
text_file.close()

text_file = open("myfile.txt","r")

# This command reads 15 characters
excerpt = text_file.read(5)
print 'Excerpt: ',excerpt

# Alternatively, we can just read data in the next line
line = text_file.readline()
print 'Line: ',line

text_file.close()
 
# or read all the lines into a list (in string format)

data_file = open("mydata.dat","r")

data = data_file.readlines()

print 'Data: ',data

print 'In For Loop:'
for line in data:
    print line,
    
# Exceptions: Let's try and break this code by trying to open a file that doesn't exist or isn't specified properly

print ''
print 'Exceptions '
print 2*bar
print ''


# Try running the script with different options for mystery file
#mysteryfile = 'mystery.txt'
#mysteryfile = 3.0
mysteryfile = 'mydata.dat'

try:
    mystery_file=open(mysteryfile,"r")
except IOError as e:
    print "This error, (",e,") means the file doesn't exist, numbnuts!"
    
except TypeError:
    print "Use a string for the filename, dumbass!" 
else:
    print "You opened the file ",mysteryfile
                    
print 'Still here'
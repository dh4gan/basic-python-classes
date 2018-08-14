# Created by Duncan Forgan 12/04/12
# Code takes as input the number of terms in the series N
# Outputs are the basic arithmetic and geometric series, 
# computed both analytically and by brute force

from math import pow  # This statement imports only one function from math
# We can use the function by typing pow(number,exponent)
# If we typed
# import math
# Then we'd have to use math.pow when we wanted to use the function


print '\t \t \t Code for calculating simple series'
print '\t \t \t ----------------------------------'

# Note the tab command \t in the strings above

N=input('How many terms are to be calculated?   ')
start=input('Where should we start from?   ')

result=start
start = 10

print 'We Begin at ', result, '\n We changed the value of start to ',start

# Simple demonstration of the if statement

if N > 100:
    print "Holy cow that's a big number!"
elif N> 10 and N <100:
    print "That's fairly big"
else:
    print "Is that all you can do?"

# Let's now calculate the arithmetic series using the for loop
for i in range(N+1):
    result=result+i
    print i, result
    
print 'The sum of the arithmetic series is ',result

# Now the geometric series.  This time we'll use a while loop

print "Now we'll do the geometric series"
a = raw_input("What is the initial value? ")  # note we're using raw_input here
r = raw_input("What is the multiplying factor? ")
N = input("How many terms? ") # Note we're using plain old input here

# raw_input delivers strings, whereas input will guess the 
# variable type from the user's input

a = float(a)
r=float(r)

i=1
result = a

while i <= N:
    result = result + a*pow(r,i)
    i+=1
    print i, result, a*pow(r,i)
    
print 'The sum of this geometric series is ',result

# Let's do some simple arithmetic to check the sum is correct
# The sum of a geometric series is s = a(1-r^N)/(1-r)

theory = a*(1.0-pow(r,N+1))/(1.0-r)

print 'The theoretical prediction is ',theory



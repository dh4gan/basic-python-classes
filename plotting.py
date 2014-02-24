# Written by Duncan Forgan, 24/02/14
# Simple script to demonstrate plotting of data in files
# This uses the numpy and matplotlib modules, which are
# extremely popular, and basically all you need to do 
# scientific computing in Python

# This code recreates the now-viral "Internet Explorer Use vs Murder Rate"
# plot that has been circling the internet

# Let's begin by importing the modules we need
# These lines mean I can use the code in the modules by using the module's "nickname"
# We'll see this in a second

import numpy as np 
import matplotlib.pyplot as plt

title='Plotting data in files'
bar = '-------'

print title
print 4*bar
print ''

# Let's define the filename for reading

inputfile='mydata.dat'

# numpy allows you to read datafiles very quickly

inputdata = np.genfromtxt(inputfile, skiprows=1)

# This makes an array with rows and columns equal to the rows and columns of the file
# The skiprows bit is optional, but lets you miss out a row if the file has a header
# (which this one does)

# To make the code clearer, we'll peel off the individual columns

years = inputdata[:,0]
internet = inputdata[:,1]
murder = inputdata[:,2]

# Let's find the maximum and minimum of each column as well

yearmin = np.amin(years)
yearmax = np.amax(years)

internetmin = np.amin(internet)
internetmax = np.amax(internet)

murdermin = np.amin(murder)
murdermax = np.amax(murder)

# We want to read the header to get the labels for our plot
# We can do this using the standard Python methods from last time

fobj = open(inputfile,"r")

# This reads all the labels into one string
line = fobj.readline()

# This splits the line string into separate strings
headers = line.split()

print "Headers before clean up "
print headers

# Now, let's tidy things up
# We should get rid of the hash here
# Also, let's replace the underscores with white space

headers = headers[1:]

for i in range(len(headers)):
    headers[i] = headers[i].replace('_', ' ')

print "Headers after clean up: " 
print headers

# Now, let's make a figure with two different y axes!
# First y axis - IE usage
# Second y axis- US murder rate

myfigure = plt.figure() # This is completely empty! No axes or anything
myfigure.suptitle("Internet Explorer Use vs US Murder Rate") # Gives the figure a title
ax = myfigure.add_subplot(111) # This adds an empty set of axes to the figure

# Now let's change some of the attributes of our plot
ax.set_xlabel(headers[0])  # Label the x axis
ax.set_xlim(yearmin,yearmax) # Set x limits
#ax.set_ylim(internetmin,internetmax) # Set y limits
ax.set_ylabel(headers[1]) # Label the y axis

# Now we plot our data

ax.plot(inputdata[:,0], inputdata[:,1], color = 'green') # Plots a simple line
ax.scatter(inputdata[:,0], inputdata[:,1], color='green', marker='*', s = 100) # Plots scatter points on the line

# This command lets us create a new axis that uses the same x-axis as "ax" 
ax2 = ax.twinx()
ax2.set_ylabel(headers[2]) # Set its label
ax2.set_ylim(murdermin,murdermax) # Set its limits

# This plots a bar chart, which is semi-transparent (thanks to the alpha command)
ax2.bar(inputdata[:,0], inputdata[:,2], facecolor='blue', alpha = 0.1, align='center')

# If we didn't do anything else, the x-axis would look a bit rubbish
# Let's fix that by making a list of strings for our x tick labels

ticklabels = [''] # We declare this with one empty entry (this is the zero tick label)

# This loop adds a string for each entry in the years array
# We make sure it
for item in years:
    ticklabels.append(str(np.int(item)))
    
print 'Our new and improved x tick labels'
print ticklabels

ax.set_xticklabels(ticklabels) # add them to plot

plt.show() # Show the figure on the screen

# This command saves the graph to a file of your choice

myfigure.savefig('IE_vs_murder.png', format='png')






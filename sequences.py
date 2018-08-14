# Written by Duncan Forgan, 25/04/12
# Simple script to demonstrate sequences
# Sequences describe multiple values in one variable, and come in a variety of forms:
# ------
# Strings
# Tuples
# Lists
# Dictionaries
# ------
# + Many other third party versions 
# (e.g. Numpy's array http://www.scipy.org/Tentative_NumPy_Tutorial)

# Some sequences are mutable (changeable), others are immutable (not changeable).

# Let's start with strings - we'll create some simple strings

title='sequence demonstrator code'
bar = '-------'

print title
print bar
print ''

# Indexing or slicing allows us to print part of the string 

print title[0]
print title[2:7]

# Negative indexing allows you to count back from the end of the string

print title[-1]

# Leaving a hanging colon lets you go right to the end of the sequence
print title[-2:]

# Strings are objects, and have associated methods 
# (go online to see http://docs.python.org/library/string.html)

print "String length is ", len(title)

shout = title.upper()
print shout
capped = title.capitalize()
print capped

search = title.count('e')
print search

# Strings are immutable - you can't change items in the sequence like this command
# The line in comments below would give an error

#title[2:5] = 'blerg'

# This is what the error would look like
#Traceback (most recent call last):
#  File "sequences.py", line 48, in <module>
#    title[2:5] = 'blerg'
#TypeError: 'str' object does not support item assignment

# However, adding new items and extending the sequence via concatenation is fine

title = title[0:2] +"_blerg_"+title[2:]
print title

# Now on to lists and tuples

print ''
print bar*5
print "Playing with Lists and Tuples"
print bar*5
print ''

mylist = ["bacon", 12, "Johnson", 34.0, "Windermere"] # Lists need square brackets
mytuple = ("bacon", 12, "Johnson", 34.0, "Windermere") # tuples don't need parenthesis, but it's much clearer to do so

print "mylist: ", mylist
print "mytuple :", mytuple

# You can create a tuple from a list
mytuple2 = tuple(mylist)

# Lists are mutable (hashable), tuples are immutable

mylist[1] = "cheese"

# This command
# mytuple[1] = "cheese"
# generates this error
# Traceback (most recent call last):
#  File "/Users/dhf/Programs/python/sequences/sequences.py", line 75, in <module>
#    mytuple[1] = "cheese"
# TypeError: 'tuple' object does not support item assignment

# You can use sequences in for loops

print "String For Loop"
for letter in title:
    print letter

print ""
print ""

print "List For Loop"
for item in mylist:
    print item*2

print ""
print ""

print "Tuple For Loop"
for item in mytuple:
    print item*4
    
print ""
print ""

# Lists and tuples have many methods in common with strings
print "Lengths: ",len(mytuple), len(mylist)

# You can append items to a list, but not a tuple

mylist.append("cheese")
del mylist[1]

print "mylist changed: ", mylist, len(mylist)

# Tuples can be added together though, to produce a similar effect

mytuple2 = mytuple2+mytuple

print "mytuple2 is now: ",mytuple2

# IMPORTANT: Lists are dynamically linked

print ""
print bar*3
print "Dynamic Linking"
print bar*3
print ""

mylist2 = mylist


mylist2[2] = "tomatoes"

# i.e. changing mylist2 changes mylist at the same time

print "mylist: ", mylist
print "mylist2: ", mylist2

# Let's now look at dictionaries
# Dictionaries have two components, an entry or value, and a key to access that entry/value
# Dictionaries are unordered, so indexing only works via keys

print ""
print bar*3
print "Dictionaries"
print bar*3
print ""


mydict = {"Boots": "something you wear on your feet", "Platypus": "An aquatic mammal that lays eggs"}

# Note that we don't reference a dictionary using a number, we use the previously defined keys
print mydict["Boots"]

# Extending a dictionary is easy

mydict["Planetesimal"]  = "A rocky/icy body up to a few kilometres in size, formed in the early stages of planet formation"
mydict["PI"] = 3.14159265
mydict["Marks"] =[24,32,1,46,55]

print "mydict has ", len(mydict), "entries"

# Some examples of dictionary methods

mykeys = mydict.keys()
myvalues = mydict.values()

print "Keys: ",mykeys
print "Values: ",myvalues

check = 'cheese' in mydict

print "Does mydict include cheese? ", check 

check = "platypus" in mydict

print "Does mydict include platypus? ",check

# This method allows you to specify what is returned if no key exists

testfail = mydict.get("cheese", "Huh?")
testsuccess = mydict.get("Platypus", "Huh?")

print testfail
print testsuccess

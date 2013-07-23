# Exercise 16 Study Drill 2
# Read the test.txt file that I just ex16.py wrote to

from sys import argv

script, filename = argv

print "I am going to read the file %r" % filename

target = open(filename, 'r')

print "Reading the file..."
print target.read()

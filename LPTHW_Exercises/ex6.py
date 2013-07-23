# assign a string variable with a string formatter
x = "There are %d types of people." % 10

# assign a string variable
binary = "binary"

# assign a string variables
do_not = "don't"

# assign a string variable, passing in the previous two variables
# as string formatters
y = "Those who know %s and those who %s." % (binary, do_not)


# print the variables x and y
print x
print y

# print a string with a string formatter x passed in via %r converter
print "I said: %r." % x

# print a string with a string formatter y passed in via %r converter
print "I also said: '%s'." % y

# assign a boolean variable False
hilarious = False

# assign a string variable with a string formatter, without providing
# it any argument
joke_evaluation = "Isn't that joke so funny?! %r"

# print the previous variable (which has a string formatter in it) and
# provide the argument
print joke_evaluation % hilarious

# assign a string variable
w = "This is the left side of..."

# assign a string variable
e = "a string with a right side."

# concatenate the previous two string variables
print w + e

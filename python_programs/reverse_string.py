# Author: Brandon Foster
# Date: December 22, 2013
#
# Reverse a string.

print "Welcome.\n"
print "I will reverse a string that you give me\n."
print "Press enter to continue or type 'exit' to leave.\n"

# Prompt user to continue or exit.
if raw_input() == "exit":
	print "Thank you. Goodbye.\n"
	quit()

# accept a string from the user
print "Please enter a string: \n"
user_string = raw_input("> ")

print "reversed string: %s\n" % user_string[::-1]
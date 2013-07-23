# Author: Brandon Foster
# Date: July 22, 2013
#
# My first python program.
# Count the number of vowels in the user's input and display it to the user.

print "\nWelcome."
print "\nI will count the number of vowels in a phrase that you give me."
print "\nPress enter to continue or type 'exit' to leave.\n"

# Prompt user to continue or exit.
if raw_input() == "exit":
	print "\nThank you. Goodbye."
	quit()

# set an array of vowels to count frequency of
vowels = ['a', 'e', 'i', 'o', 'u']

# count number of vowels in given input string
def count_vowels(phrase_to_count):
	count = 0
	for i in range(0, len(vowels)):
		count += phrase_to_count.count(vowels[i])
	return count
		

# accept phrase from user to count vowels for
print "\nPlease enter a phrase: "
phrase = raw_input("\n> ")

# set num_vowels to return value of count_vowels(string) method
num_vowels = count_vowels(phrase)

print "\nNumber of vowels: %d" % num_vowels

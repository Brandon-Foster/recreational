from sys import argv

# passing in a filename to read via command line argument
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()

# passing in a filename to read through raw_input argument
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

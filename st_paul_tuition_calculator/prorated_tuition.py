# Author: Brandon Foster
# Date: July 22, 2013
#
# Calculate prorated tuition of a given month for a child at St. Paul School

from datetime import date

months = {
	1: 'January',
	2: 'February',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December'
}

# Accepts the starting year
print ("\nPlease enter the year the student began. (i.e., 2013)")

year = int(raw_input("\n> "))

print "\nYou entered %d." % (year)

# Accepts the starting month
print ("\nPlease enter the month the student began. (January would be 1)")

month = int(raw_input("\n> "))

print "\nYou entered %d: %s." % (month, months[month])

# Accepts the starting date
print ("\nPlease enter the start date of the student.")

date = int(raw_input("\n> "))

print "\nThe date you entered is: %d." % (date)

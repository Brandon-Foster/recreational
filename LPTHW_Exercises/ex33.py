def loop_function(upper):
	i = 0
	numbers = []	

	for i in range(0, upper):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
		
loop_function(10)

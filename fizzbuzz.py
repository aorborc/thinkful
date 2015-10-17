import sys
n = int(raw_input("Enter the Counter number : "))
for i in range(1,n):
	if( i% 15 == 0):
		print "fizzbuzz"
	elif (i%3 == 0):
		print "fizz"
	elif (i%5 == 0):
		print "buzz"
	else:
		print i


def isBouncy(digit):
	inc = False 
	dec = False
	while(digit//10>0):
		num1 = digit%10
		digit = digit//10
		num2 = digit%10
		if(num2>num1):
			# print("{} > {}".format(num2, num1))
			dec = True
		if(num2<num1):
			# print("{} < {}".format(num2, num1))
			inc = True
	return (inc and dec)

prop = 0
b = 0
digit = 0
pc = 99.0
while(prop < pc):
	digit = digit + 1
	b = b + isBouncy(digit)
	prop = 100*float(b)/digit
	# print(prop)

# print(prop)
print(digit)
# answer: 1587000
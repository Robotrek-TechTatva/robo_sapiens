import csv
with open('points.csv') as file:
	reader = csv.reader(file, delimiter=',')
	a = 0
	b = 0
	for match in reader:
		if(match[0] == "Serial"):
			continue
		# print(match)
		a = a + int(match[1])
		b = b + int(match[2])

print(a)
print(b)
if(a>b):
	print("Winner of match: A")
elif(b>a):
	print("Winner of match: B")
else:
	print("Draw")


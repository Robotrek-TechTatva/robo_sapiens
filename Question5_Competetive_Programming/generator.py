import csv
import random

# field names
#Coordinates of vertices are (X1, Y1), (X2, Y2) and (X3, Y3)
fields = ['Serial', 'A', 'B']
rows=[]

i=0
while i<random.randint(24, 500):
    A=random.randint(0 ,1)

    if A is 1:
        B=0
    else:
        B=1

    rows.append([str(i), str(A), str(B)])
    i+=1

# name of csv file
filename = "points.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

import csv
import random

# field names
#Coordinates of vertices are (X1, Y1), (X2, Y2) and (X3, Y3)
fields = ['Serial', 'X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3']
rows=[]
# data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
#          ['Sanchit', 'COE', '2', '9.1'],
#          ['Aditya', 'IT', '2', '9.3'],
#          ['Sagar', 'SE', '1', '9.5'],
#          ['Prateek', 'MCE', '3', '7.8'],
#          ['Sahil', 'EP', '2', '9.1']]
#
# rows.append(['Raghav', 'd', '3', str(7)])

i=0
while i<25:
    X1 = random.randint(-100,100)
    X2 = random.randint(-100,100)
    X3 = random.randint(-100,100)

    Y1 = random.randint(-100,100)
    Y2 = random.randint(-100,100)
    Y3 = random.randint(-100,100)

    rows.append([str(i), str(X1), str(Y1), str(X2), str(Y2), str(X3), str(Y3)])
    i+=1

# name of csv file
filename = "traingles.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

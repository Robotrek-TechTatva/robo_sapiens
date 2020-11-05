import csv
_inp=input()
with open(_inp) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x1 = []
    y1 = []
    i=0
    for column in readCSV:

        x1.append(column)


    tri=x1[1:]


def area(x1, y1, x2, y2, x3, y3): 
  
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0) 
  
  
# A function to check whether point P(x, y) 
# lies inside the triangle formed by  
# A(x1, y1), B(x2, y2) and C(x3, y3)  
def isInside(x1, y1, x2, y2, x3, y3, x, y): 
  
    # Calculate area of triangle ABC 
    A = area (x1, y1, x2, y2, x3, y3) 
  
    # Calculate area of triangle PBC  
    A1 = area (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC  
    A2 = area (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = area (x1, y1, x2, y2, x, y) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False


count=0
for i in range(len(tri)):
    x_1=int(tri[i][0])
    y_1=int(tri[i][1])
    x_2=int(tri[i][2])
    y_2=int(tri[i][3])
    x_3=int(tri[i][4])
    y_3=int(tri[i][5])
    if(isInside(x_1, y_1, x_2, y_2, x_3, y_3, 0,0)):
        count+=1
print(count)

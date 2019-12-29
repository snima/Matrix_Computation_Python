import random
R = int(input("Enter First Dimantion:"))
C = int(input("Enter Second Dimention:"))
P_Z = int(input("Enter Probablity Weight of Zero (e.g. 1):"))
P_O = int(input("Enter Probablity Weight of One (e.g. 2):"))
matrix = []
mylist = [0, 1]
T=R*C
data=random.choices(mylist, weights = [int(P_Z), int(P_O)], k=T )

for i in range(R):          
    a =[] 
    for j in range(C):       
         a.append(int(data[(i-1)*j+j])) 
    matrix.append(a) 

#Printing the Matrix
print("Random Matrix ")
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

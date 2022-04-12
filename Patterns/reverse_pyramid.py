n = int(input("Enter Number of rows : "))
for i in range (0, n) :
    for j in range (0,i) :
        print(end=" ")
    for k in range (0, n-i) :
        print(i+1, end=" ")
    print()
    
    
"""
for n = 5
output :
1 1 1 1 1 
 2 2 2 2 
  3 3 3 
   4 4 
    5 
"""

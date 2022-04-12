n = int(input("Enter Number of rows : "))
for i in range (0, n) :
    for j in range (0,i) :
        print(end=" ")
    for k in range (0, n-i) :
        print(n-i, end=" ")
    print()
    
    
"""
for n = 7
output :
7 7 7 7 7 7 7 
 6 6 6 6 6 6 
  5 5 5 5 5 
   4 4 4 4 
    3 3 3 
     2 2 
      1
"""

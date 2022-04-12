r = int(input("Enter Number of rows : "))
if r%2==0 :
    n=(r//2)
    for i in range(0, n):
    	for j in range(0, n-i-1):
    		print(end=" ")
    	for k in  range(0, i+1):
    		print (i+1, end=" ")
    	print()
    for i in range (0, n) :
        for j in range (0,i) :
            print(end=" ")
        for k in range (0, n-i) :
            print(n-i, end=" ")
        print()
else :
    n=(r+1)//2
    for i in range(0, n):
    	for j in range(0, n-i-1):
    		print(end=" ")
    	for k in  range(0, i+1):
    		print (1+i, end=" ")
    	print()
    for i in range (1, n) :
        for j in range (0,i) :
            print(end=" ")
        for k in range (0, n-i) :
            print(n-i, end=" ")
        print()
        
        
"""
for r = 9
output :
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1 
for r = 6
output :
  1 
 2 2 
3 3 3 
3 3 3 
 2 2 
  1 
"""

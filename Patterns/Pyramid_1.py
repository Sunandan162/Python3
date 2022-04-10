n = int(input("Enter number of rows : "))
for i in range(0, n):
	for j in range(0, n-i-1):
		print(end=" ")
	for k in  range(0, i+1):
		print (k+1, end=" ")
	print()
    
    
    
"""
output-
n=6
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
1 2 3 4 5 6 

"""

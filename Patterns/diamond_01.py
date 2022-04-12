r = int(input("Enter Number of rows : "))
n = (r+1)//2
for i in range(0, n):
	for j in range(0, n-i-1):
		print(end=" ")
	for k in  range(0, i+1):
		print (i+1, end=" ")
	print()
i = 0 if r %2 == 0 else 1  #for reverse pyramid
for i in range (i, n) :
    for j in range (0,i) :
        print(end=" ")
    for k in range (0, n-i) :
        print(n-i, end=" ")
    print()




"""
for r = 7
output :

   1 
  2 2 
 3 3 3 
4 4 4 4 
 3 3 3 
  2 2 
   1 
for r = 6
   1 
  2 2 
 3 3 3 
 3 3 3 
  2 2 
   1 
"""

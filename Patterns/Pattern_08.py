n = int(input("Enter Number of rows : "))
for i in range (0,n+1):
    for j in range (0,i):
        print("*",end="")
    for k in range (0,(2*n)-(2*i)):
        print(end=" ")
    for l in range (0,i):
        print("*",end="")
    print()
    
    
"""
for n = 6
Output :
*          *
**        **
***      ***
****    ****
*****  *****
************
"""

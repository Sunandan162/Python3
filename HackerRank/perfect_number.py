n=int(input("number : "))
s=0
for i in range (1,n):
    r=n%i
    if r==0:
        s=s+i
if s==n:
    print("perfect")
else:
    print("no")
    
    
"""
Input :
number : 8128
Output:
perfect
"""

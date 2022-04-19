n=int(input("Nuber of rows :")) #number of rows must be less than 10
for i in range(1,n+1):
    for j in range (1,i+1):
        print (j,end="")
    for k in range (1,i):
        print(i-k,end="")
    print()
    
    
"""
Nuber of rows :5
1
121
12321
1234321
123454321
"""

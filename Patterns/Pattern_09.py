n=int(input("rows= "))
for i in range (0,n+1):
        for j in range (0,i):
            if i < 10:
                print(i,end="  ")
            else:
                print(i,end=" ")
        for k in range (0,(2*n)-(2*i)):
            print(end="   ")
        for l in range (0,i):
            if i < 10:
                print(i,end="  ")
            else :
                print(i,end=" ")
        print()
        
        
"""
for n =12
                                                                        
1                                                                    1  
2  2                                                              2  2  
3  3  3                                                        3  3  3  
4  4  4  4                                                  4  4  4  4  
5  5  5  5  5                                            5  5  5  5  5  
6  6  6  6  6  6                                      6  6  6  6  6  6  
7  7  7  7  7  7  7                                7  7  7  7  7  7  7  
8  8  8  8  8  8  8  8                          8  8  8  8  8  8  8  8  
9  9  9  9  9  9  9  9  9                    9  9  9  9  9  9  9  9  9  
10 10 10 10 10 10 10 10 10 10             10 10 10 10 10 10 10 10 10 10 
11 11 11 11 11 11 11 11 11 11 11       11 11 11 11 11 11 11 11 11 11 11 
12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 
"""

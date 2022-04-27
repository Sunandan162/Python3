#problem - https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

y=int(input())
leap=False
if y==1918:
    print("26.09.",end="")
    print(y)
elif y>1918:
    if y % 400 == 0 :
            leap = True
    elif y %100 != 0 and y % 4 == 0 :
        leap = True
    else :
        leap = False  
elif y<=1917:
    leap=False
    if y % 4 == 0 :
        leap = True
    else :
        leap = False   
if y != 1918:
    if leap==True:
        print("12.09.",end="")
    else:
        print("13.09.",end="")
    print(y)

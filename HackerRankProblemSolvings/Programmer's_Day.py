#problem - https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

y=int(input())
if y>1918:
    leap=False
    if y % 100 == 0:
        if y % 400 == 0 :
            leap = True
    elif y % 4 == 0 :
        leap = True
    else :
        leap = False   
    if leap==True:
        print("12.09.",end="")
    else:
        print("13.09.",end="")
    print(y)
else:
    print("12.09.",end="")
    print(y)

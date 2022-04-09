def is_leap(y):
    leap = False
    if y % 100 == 0:
        if y % 400 == 0 :
            leap = True
    elif y % 4 == 0 :
        leap = True
    else :
        leap = False   
    return leap

year = int(input())
print(is_leap(year))

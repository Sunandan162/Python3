#problem : https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    s = input()
    a = False
    for i in s:
        if i.isalnum():
            a = True 
            break
    print(a)
    a = False
    for i in s:
        if i.isalpha():
            a = True 
            break
    print(a)
    a = False
    for i in s:
        if i.isdigit():
            a = True 
            break
    print(a)
    a = False
    for i in s:
        if i.islower():
            a = True 
            break
    print(a)
    a = False
    for i in s:
        if i.isupper():
            a = True 
            break
    print(a)

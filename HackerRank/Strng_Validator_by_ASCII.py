if __name__ == '__main__':
    s = input()
    a = False
    for i in s:
        if ord(i) in range(65,91) or ord(i) in range (97,123) or ord(i) in  range(48,58):
            a = True 
            break
    print(a)
    a = False
    for i in s:
         if ord(i) in range(65,91) or ord(i) in range(97,123):
            a = True 
            break
    print(a)
    a = False
    for i in s:
         if ord(i) in  range(48,58):
            a = True 
            break
    print(a)
    a = False
    for i in s:
     if ord(i) in range(97,123):
            a = True 
            break
    print(a)
    a=False
    for i in s:
         if ord(i) in range(65,91):
            a = True 
            break
    print(a)

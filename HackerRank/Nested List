#problem-  https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    r=[] #r is the marksheet list
    b=[] # b is the list to store  names of second lowest
    sl = None
    for t in range(int(input())): #t for total number of entry
        name = input()
        score = float(input())
        a=[name,score]
        r.append(a)
        r.sort(key = lambda x: x[1])
    for x in r:
        if r[0][1] < x[1]:
            sl = x[1]
            break
    for x in r:
        if sl == x[1] :
          b.append(x[0])
    b.sort()
    for x in b:
        print(x)

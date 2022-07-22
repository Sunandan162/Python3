#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    a=[]
    for i in range (N):
        entry=input().rstrip().split()
        cmnd=entry[0]
        if cmnd=="pop":
            a.pop(-1)
        elif cmnd=="append":
            a.append(int(entry[1]))
        elif cmnd=="remove":
            a.remove(int(entry[1]))
        elif cmnd=="insert":
            a.insert(int(entry[1]),int(entry[2]))
        elif cmnd=="sort":
            a.sort()
        elif cmnd=="reverse":
            a.reverse()
        elif cmnd=="print":
            print(a)

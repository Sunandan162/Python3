#problem- https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
ar.sort()
p=c=0
for i in range(0,n-1):
    if ar[i]!=c:
        c=ar[i]
        a=ar.count(ar[i])
        p=p+(a//2)
print(p)

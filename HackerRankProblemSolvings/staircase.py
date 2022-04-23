#problem- https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


n=int(input())
for i in range (0,n):
    for j in range (0,n-i-1):
        print(end=" ")
    for k in range (0,i+1):
        print("#",end="")
    print()

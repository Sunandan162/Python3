#problem- https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

x1=int(input())
v1=int(input())
x2=int(input())
v2=int(input())
s1=(x1+v1)
s2=(x2+v2)
if s1%s2==0:
    print('Yes')
elif s2%s1==0:
    print('Yes')
else:
    print('No')

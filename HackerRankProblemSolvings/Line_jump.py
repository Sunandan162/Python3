#problem- https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])
s1=(x1+v1)
s2=(x2+v2)
print('YES') if s1%s2==0 or s2%s1==0 else print('NO')

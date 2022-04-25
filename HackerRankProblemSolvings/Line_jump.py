#problem- https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])
if (v1 > v2):
    if (x1 - x2) % (v2 - v1) == 0:
        print('YES')
    else:
        print("NO")
else:
    print("NO")

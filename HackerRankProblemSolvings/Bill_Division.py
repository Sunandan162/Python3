#problem - https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())
a = sum(bill) - bill[k]
if b == a/2:
    print("Bon Appetit")
else:
    print(int(b-(a/2)))

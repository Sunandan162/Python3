#problem - https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


a = list(map(int, input().rstrip().split()))
a.sort()
print(sum(a)-a[-1], sum(a)-a[0])

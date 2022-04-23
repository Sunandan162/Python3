#problem - https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
if 'P' in time:
    if h in range (1,12):
        h = h+12        
else:
    if h == 12:
        h = 0
print(('%02d:%02d:%02d') % (h, m, s))

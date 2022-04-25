#problem - https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
for x in grades:
    if x < 38 or (((x//5)+1)*5)-x >= 3:
        print(x)
    else:
        print(((x//5)+1)*5)

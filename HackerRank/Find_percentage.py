#problem - https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    x = student_marks.get(input())
    print('%.2f'%(sum(x)/len(x)))

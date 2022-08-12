#prob- https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    str1=""
    string=list(s)
    position=int(i)
    charecter=c
    string[position]=charecter
    new_s=str1.join(string)
    return new_s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

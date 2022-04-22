#problem - https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def plusMinus(arr):
    j=0
    k=0
    l=0
    for i in arr:
        if i < 0:
            j = j+1
        elif i > 0:
            k = k+1
        elif i == 0:
            l = l+1
    print (k/n)
    print (j/n)
    print (l/n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

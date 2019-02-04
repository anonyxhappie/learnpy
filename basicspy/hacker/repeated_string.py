#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # infi_string = ""
    s_len = len(s)
    a_count = 0
    r_count = 0
    result = 0

    if s_len == 1 and s[0] == 'a':
        return n

    d = n // s_len
    r = n % s_len

    for i in range(s_len):
        if (s[i] == 'a'):
            a_count += 1
    
    for i in range(r):
        if (s[i] == 'a'):
            r_count += 1
    
    result = d * a_count + r_count

    return result
    # abcac abcac abc

    # for i in range(n):
    #     if (j == s_len):
    #         j = 0
        
    #     if (s[j] == 'a'):
    #         a_count += 1

    #     # infi_string += s[j]
    #     j += 1
    
    # return a_count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input() 

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()


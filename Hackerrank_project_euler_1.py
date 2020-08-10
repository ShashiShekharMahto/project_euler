#!/bin/python3

import sys
from math import floor

def s(n):
        
    a = floor((n-1)/5)
    b = floor((n-1)/3)
    c = floor((n-1)/15)
    s5 = a*(5+5*a)
    s3 = b*(3+3*b)
    s15 = c*(15+15*c)
    print(int(int(s5+s3-s15)>>1))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s(n)


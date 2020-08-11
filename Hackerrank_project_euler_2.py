#!/bin/python3

import sys

def fibSum(n):
    a=[1,2]
    b = [2]
    i=1

    while(a[i]<n):
        bnext = 3*a[i]+2*a[i-1]
        anext = 2*a[i]+a[i-1]
        a.append(anext)
        a.append(bnext)
        if(bnext<n):
            b.append(bnext)
        i = i+2
    print(sum(b))


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibSum(n)

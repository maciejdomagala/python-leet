
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter



############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def insr2():
    s = input()
    return(s.split(" "))

def prime_factorization(n):

    if n == 1:
        return [1]

    ans=[]
    i = 2
    cap = sqrt(n)
    while i <= cap:
        if n % i == 0:
            ans.append(i)
            n = n//i
            cap=sqrt(n)
        else:
            i += 1
    if n > 1:
        ans.append(n)
    return ans

def binomial(n, k):
    if n == 1 or n == k:
        return 1

    if k > n:
        return 0       
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n-k)
        div = a // (b * c)
        return div 

for _ in range(inp()):
    n= inp()
    a = insr()
    b = insr()

    opsa, opsb=[],[]

    for i in range(n-1):
        if a[i] != a[i+1]:
            opsa.append(i+1)
        if b[i] != b[i+1]:
            opsb.append(i+1)

    if b[-1] != a[-1]:
        opsb.append(n)

    ans = opsa + opsb[::-1]
    ans.insert(0, len(ans))
    
    print(' '.join([str(a) for a in ans]))

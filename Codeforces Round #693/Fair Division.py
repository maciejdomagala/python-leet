
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

def prefix(arr):
    return [sum(arr[:i]) for i in range(1, n+1)]  
    
for _ in range(inp()):
    n = inp()
    arr = invr()
    c1, c2 = 0,0
    for a in arr:
        if a == 1:
            c1 += 1
        else:
            c2 += 1

    if c1 % 2 == 0:
        if c2 % 2 == 0:
            print 'YES'
            continue
        else:
            if c1 > 0:
                print 'YES'
                continue
    
    print 'NO'
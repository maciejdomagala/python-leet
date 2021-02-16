
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
    n = inp()
    arr = invr()
    count=0
    c0,c1,c2 = 0,0,0
    for a in arr:
        if a % 3 == 0:
            c0+=1
        elif a % 3 == 1:
            c1 += 1
        else:
            c2 += 1

    mx = max(c0,c1,c2)
    if c0 == mx:
        count += n//3-c1
        count+= 2*(n//3-c2)
    elif c1 == mx:
        count += n//3-c2
        count+= 2*(n//3-c0)    
    else:
        count += n//3-c0
        count+= 2*(n//3-c1)

    print count
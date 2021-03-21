
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict
from copy import deepcopy as dc
# from statistics import median, mean


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

a = raw_input()

for _ in range(inp()):

    n = inp()
    a = invr()
    f = False

    c, k = -1,-1
    incr, dcr = 0,0

    mx = a[0]

    for i in range(1,n):
        if a[i] > mx:
            mx = a[i]
        if a[i] >= a[i-1]:
            incr += 1
            if c == -1:
                c = a[i]-a[i-1]
            else:
                if c != (a[i]-a[i-1]):
                    f = True
                    break
        if a[i] < a[i-1]:
            dcr += 1
            if k == -1:
                k = a[i-1]-a[i]
            else:
                if k != (a[i-1]-a[i]):
                    f = True
                    break
    if f == True:
        print -1
        continue

    if dcr == 0 or incr == 0:
        print 0
        continue

    if c+k > mx:
        print c+k, c
    else:
        print -1
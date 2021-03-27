
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
from copy import deepcopy as dc


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


r = raw_input()
n = inp()
arr = invr()
ans = []

i, j = 0, n-1
mn = 0
while i <= j:
    a = arr[i]
    b = arr[j]

    if mn >= max(a,b):
        break
    elif mn < min(a,b):
        if a < b:
            mn = a
            ans.append('L')
            i += 1
        elif a > b:
            mn = b
            ans.append('R')
            j -= 1
    else:
        if a > mn:
            mn = a
            ans.append('L')
            i += 1
        else:
            mn = b
            ans.append('R')
            j -= 1

print len(ans)
print ''.join(ans)
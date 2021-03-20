
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict
from copy import deepcopy as dc
# import numpy as np
# from operator import itemgetter 
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

n = inp()
arr = invr()
q = inp()

ca = Counter(arr)
s, r =0,0
for a in ca:
    s += ca[a] // 4
    if ca[a] % 4 > 1:
        r += 1

for _ in range(q):
    query = raw_input()
    sign = query[0]
    value = int(query[2:])
    
    if sign == '+':
        s -= ca[value] // 4
        r -= ca[value] % 4 > 1

        ca[value] += 1

        s += ca[value] // 4
        r += (ca[value] % 4) > 1

    if sign == '-':
        s -= ca[value] // 4
        r -= ca[value] % 4 > 1

        ca[value] -= 1

        s += ca[value] // 4
        r += (ca[value] % 4) > 1

    if s > 1:
        print 'YES'
    elif s < 1:
        print 'NO'
    else:
        if r > 1:
            print 'YES'
        else:
            print 'NO'

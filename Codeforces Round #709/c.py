
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict
from copy import deepcopy as dc
# from statistics import median, mean

inf = float('inf')
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

    n, m = invr()
    
    d = defaultdict(int)
    ans = []

    for i in range(m):
        arr = invr()
        k = arr[0]
        arr = arr[1:]
        ind = arr[0]
        mn = inf

        for i in range(k):
            value = d[arr[i]]
            if value < mn:
                mn = value
                ind = arr[i]

        d[ind] += 1
        ans.append(ind)
        if d[ind] > int(ceil(m/2)):
            print "NO"
            break
    else:
        print 'YES'
        print ' '.join([str(a) for a in ans])

        
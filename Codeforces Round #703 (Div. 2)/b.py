
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
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

for _ in range(inp()):
    n = inp()
    xs = []
    ys = []
    c=0
    pairs = []
    for _ in range(n):
        x, y = invr()
        xs.append(x)
        ys.append(y)

    if len(set(xs)) == 1 and (set(xs) == set(ys)):
        print 1
        continue
    if len(set(xs)) == 1:
        print max(ys)-min(ys)+1
        continue
    elif len(set(ys)) == 1:
        print max(xs)-min(xs)+1
        continue

    if n%2 == 0:
        mid_x = [xs[int(n//2)],xs[int(n//2)-1]]
        mid_y = [ys[int(n//2)],ys[int(n//2)-1]]
        print len(set(mid_x))*len(set(mid_y))
    else:
        print 1


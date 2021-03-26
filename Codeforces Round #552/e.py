
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque
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


# r = raw_input()

n, k = invr()
s = raw_input()

d = [s]
vis = {s}

cost = 0
c = 0

while c < k and d:
    cur = d.pop(0)
    cost += n - len(cur)
    c += 1
    for i in range(len(cur)):
        element = cur[:i] + cur[i+1:]

        if element not in vis:
            vis.add(element)
            d.append(element)


print -1 if c<k else cost
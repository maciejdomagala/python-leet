
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque, defaultdict
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

#
# r = raw_input()
        
for _ in range(inp()):
    n, w = invr()
    arr = invr()

    arr.sort(reverse=True)

    ca = Counter(arr)

    keys = [a for a in ca]
    keys.sort(reverse=True)

    s = sum(arr)
    i = 0
    count = 0

    while s > 0:
        count += 1
        cur = w 
        i = 0
        while i < len(keys):
            element = keys[i]
            if ca[element] == 0:
                i += 1
                continue
            else:
                if element <= cur and ca[element] > 0:
                    cur -= element
                    s -= element
                    ca[element] -= 1
                else:
                    i += 1
                    continue
        
    print count
        




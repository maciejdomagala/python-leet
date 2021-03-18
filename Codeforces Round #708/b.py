
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

for _ in range(inp()):

    temp = defaultdict(int)
    c = 0

    n, m = invr()
    arr = invr()
    ans = 0

    for a in arr:
        temp[a%m] += 1

    for i in range(1, int(ceil((m//2)))):
        mx, mn = max(temp[i], temp[m-i]), min(temp[i], temp[m-i])
        ans += max(1, mx-mn)
    

    if temp[0] > 0:
        ans += 1
    if n%2 == 0:
        if temp[m//2] > 0:
            ans += 1

    print ans



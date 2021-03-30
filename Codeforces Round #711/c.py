
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque, defaultdict
from copy import deepcopy as dc

# sys.setrecursionlimit(10**6)


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

def prefix(arr):

    return [sum(arr[:i+1]) for i in range(len(arr))]

for _ in range(inp()):
    n, k = invr()

    if k == 1:
        print 1
        continue
    if n == 1:
        print 2
        continue

    #from now on, assume n and k are >= 2.

    arr = [1] + [0]*(n-2)
    ans = 2
    deq = deque(arr)
    
    while k > 1:
        temp = 0
        for i in range(n-1):
            temp += deq.popleft()
            deq.append(temp)
            ans += temp

        deq.reverse()
        temp = 0
        k -= 1

    print ans % (10**9+7)





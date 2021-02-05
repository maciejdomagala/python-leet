
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
    s = raw_input()
    curr = 1
    q0, q1 = [],[]
    ans = []

    for i, a in enumerate(s):
        if a == '0':
            if len(q1) == 0:
                ans.append(curr)
                q0.append(curr)
                curr += 1
            else:
                seq = q1.pop()
                ans.append(seq)
                q0.append(seq)
        if a == '1':
            if len(q0) == 0:
                ans.append(curr)
                q1.append(curr)
                curr += 1
            else:
                seq = q0.pop()
                ans.append(seq)
                q1.append(seq)
    
    print max(ans)
    print ' '.join([str(a) for a in ans])
                
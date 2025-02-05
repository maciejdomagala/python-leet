
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict
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

def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd


# r = raw_input()

for _ in range(inp()):
    n = inp()
    z = prime_factorization(n)
    ans = set()
    temp = 1

    for i, a in enumerate(z):
        if len(ans) >= 2:
            temp *= a
        else:
            if a not in ans:
                ans.add(a)
            else:
                temp *= a
                if temp not in ans:
                    ans.add(temp)
                    temp = 1

    if temp != 1 and temp not in ans and len(ans) == 2:
        ans.add(temp)
        print 'YES'
        print ' '.join(str(a) for a in list(ans))
    else:
        print 'NO'



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

#if s = 0 => -1 both

#for max
m, s = invr()
h = dc(s)

if s == 0:
    if m == 1:
        print 0, 0
    else:
        print -1, -1
    sys.exit()

if 9*m < s:
    print -1, -1
    sys.exit()
    
ans = []
i = 0
while i < m:
    if s >= 9:
        ans.append(9)
        s -= 9
    else:
        ans.append(s)
        s = 0

    i += 1

if s > 0:
    mx = -1

#for min
mn = ans[::-1]

if mn[0] == 0:
    i = 1
    while i < len(ans):
        if mn[i] != 0:
            mn[i] -= 1
            mn[0] = 1
            break

        i += 1

print ''.join([str(a) for a in mn]), ''.join([str(a) for a in ans])

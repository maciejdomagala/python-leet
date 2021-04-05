
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
    n = inp()
    s = raw_input()

    ones = s.count('1')

    ans1 = []
    ans2 = []

    c0 = 0
    c1 = 0

    if s[0] != '1' or s[-1] != '1':
        print 'NO'
        continue

    if ones % 2 == 1:
        print 'NO'
        continue

    for a in s:
        if a == '1':
            c1 += 1
            if c1 <= ones//2:
                ans1.append('(') 
                ans2.append('(') 
            else:
                ans1.append(')') 
                ans2.append(')') 
        else:
            c0 += 1
            if c0 % 2 == 1:
                ans1.append('(')
                ans2.append(')')
            else:
                ans2.append('(')
                ans1.append(')')

    print 'YES'
    print ''.join(ans1)
    print ''.join(ans2)

from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
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

for _ in range(inp()):
    s = insr()
    a,b,c = 0,0,0
    f = True
    if s[0] == s[-1]:
        print 'NO'
        continue

    d = {}
    d['a'] = 0
    d['b'] = 0
    d['c'] = 0

    for i in s:
        if i == 'A':
            d['a'] += 1
        elif i == 'B':
            d['b'] += 1
        else:
            d['c'] += 1

    ans = ''

    first = s[0]
    last = s[-1]

    count= 0

    for i in s:
        if i == first:
            count += 1
        elif i == last:
            count -= 1
        else:
            if s.count(first) > s.count(last):
                count -= 1
            elif s.count(first) < s.count(last):
                count += 1
            else:
                print 'NO'
                f = False
                break

        if count < 0:
            print 'NO'
            f = False
            break

    if f == True and count != 0:
        print 'NO'
    elif f == True and count == 0:
        print 'YES'
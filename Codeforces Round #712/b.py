
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
    f = True
    ans = True
    a = raw_input()
    b = raw_input()

    i = 0
    pre = []
    val = []

    ind = set()

    if a[0] == b[0]:
        f = True
    else:
        f = False

    if a[0] == '0':
        c0, c1 = 1, 0
    else:
        c0, c1 = 0, 1

    for i in range(1, n):
        if a[i] == '0':
            c0 += 1
        else:
            c1 += 1

        if c0 == c1:
            ind.add(i)

        if a[i] == b[i]:
            if f == True:
                continue
            else:
                if (i-1) in ind:
                    f = True
                    continue
                else:
                    ans = False
                    break     
        elif a[i] != b[i]:
            if f == False:
                continue
            else:
                if (i-1) in ind:
                    f = False
                    continue
                else:
                    ans = False
                    break
        


    if f == False:
        if n-1 not in ind:
            print 'NO'
            continue

    if ans:
        print 'YES'
    else:
        print 'NO'



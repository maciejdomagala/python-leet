
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

#
# r = raw_input()
        
for _ in range(inp()):
    s = insr()

    ca = Counter(s)
    ans = []

    if ca['L'] > ca['R']:
        ca['L'] -= (ca['L']-ca['R'])
    elif ca['L'] < ca['R']:
        ca['R'] -= (ca['R']-ca['L'])

    if ca['U'] > ca['D']:
        ca['U'] -= (ca['U']-ca['D'])
    elif ca['U'] < ca['D']:
        ca['D'] -= (ca['D']-ca['U'])
        
    if ca['U'] == 0:
        if ca['L'] > 0:
            print 2
            print 'LR'
        else:
            print 0
    elif ca['L'] == 0:
        if ca['U'] > 0:
            print 2
            print 'UD'
        else:
            print 0
    else:
        print sum(ca.values())
        print 'U'*ca['U']+'R'*ca['R']+'D'*ca['D']+'L'*ca['L']

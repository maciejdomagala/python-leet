
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
    n = inp()
    arr = invr()
    ans = 0

    ca= Counter(arr)

    zz = ca.most_common()

    mx = 0 #number of max occurencies
    rest = 0 #number of rest of the values
    for a,b in zz:
        if b == zz[0][1]:
            mx += 1
        else:
            rest += b

    """
    4
    7
    1 7 1 6 4 4 6
    """


    #when we have number of max values, we are grouping them together
    #and the answer will be the min number of rest of numbers divided slots between (mx-1) 

    groups = zz[0][1]-1
    ans = rest//groups

    #and if the number of max numbers is greater than 1, we need to include the additional space

    ans += (mx-1)
    
    print ans


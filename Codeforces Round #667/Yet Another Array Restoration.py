
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
    n, a, b = invr()
    k = n-1
    counter = n-1
    ret = 0

    while k > 0:
        if (b-a) % k == 0:
            ret = k
            break
        else:
            k -= 1

    if k == 1:
        ret=1

    divisor = (b-a)//ret
    ans = []
    c=1
    mod = b % divisor
    if mod == 0:
        mod = divisor
    ans = [mod]
    while c < n:
        ans.append(c*divisor + mod)
        c += 1

    add_value = max(0, b-max(ans))
    ans = [a+add_value for a in ans]
    
    print ' '.join([str(a) for a in ans])

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
    n, k = invr()
    b = raw_input()

    if b.count('1') == 0:
        print len(b)//k
        continue

    b = b.split('1')

    for i in range(len(b)):
        if i == 0:
            b[i] = len(b[i])-k
        elif i == len(b)-1:
            b[i] = len(b[i])-k
        else:
            b[i] = len(b[i])-2*k

    ans = 0

    for a in b:
        if a > 0:
            ans+=a//k

    print ans




    
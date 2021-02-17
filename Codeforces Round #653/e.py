
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict



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


n,k = invr()
both, al, bob = [],[],[]
c = 0
for __ in range(n):
    t, a ,b = invr()

    if a == b == 1:
        both.append(t)
    elif a == 1:
        al.append(t)
    else:
        bob.append(t)

f = True

both.sort()
al.sort()
bob.sort()

blen = len(both)
allen = len(al)
boblen = len(bob)

i = 0
while i < k:
    if blen == 0 and (boblen == 0 or allen == 0):
        f = False
        break

    if blen == 0:
        c += al.pop(0)
        c += bob.pop(0)
        boblen -= 1
        allen -= 1
    elif (boblen == 0 or allen == 0):
        c += both.pop(0)
        blen -= 1
    else:
        if both[0] <= al[0] + bob[0]:
            c+= both.pop(0)
            blen -= 1
        else:
            c += al.pop(0)
            c += bob.pop(0)
            boblen -= 1
            allen -= 1

    i += 1

if f == True and i == k:
    print c
else:
    print -1

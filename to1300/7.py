
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
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

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

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

def small_divisor(n):

    if n % 2 == 0:
        return 2

    i = 3
    while i*i <= n:
        if n%i == 0:
            return i
        i += 2

    return n

n = inp()
arr = invr()

if n == 1:
    if arr[0] == 1:
        print 0
        sys.exit()
    else:
        print 1
        sys.exit()

cur, mx = 0,0
ones = 0

for i in range(n):
    if arr[i] == 0:
        cur += 1
        if mx < cur:
            mx = cur
    else:
        ones += 1
        cur -= 1
        if cur < 0:
            cur = 0

if mx == 0:
    print n-1
else:
    print ones+mx
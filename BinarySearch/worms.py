
from __future__ import division
import sys
input = sys.stdin.readline
from sys import stdout
import math
from math import sqrt, floor, ceil
from collections import Counter
from copy import deepcopy as dc
from bisect import bisect
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

def rwh_primes1(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

def sieve(n):
    arr=[1]*(n+1)
    arr[1]=0
    for i in range(2,int(math.sqrt(n+1))+4):
        if arr[i]==1:
            for j in range(2*i,n+1,i):
                arr[j]=0
    return arr

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

def binary_search(a,x,lo=0,hi=-1):
    i = bisect(a,x,lo,hi)
    if i == 0:
        return -1
    elif a[i-1] == x:
        return i-1
    else:
        return -1


n = inp()
arr = invr()
m = inp()
qs = invr()

d = {}

c = 0
for i in range(sum(arr)+1):
    if i > sum(arr[:c]):
        c += 1
    d[i] = c

d[0] = 1

for a in qs:
    print d[a]
    

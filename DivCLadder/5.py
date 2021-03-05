
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

def comb(x):

    return x*(x-1)//2

n = inp()
arr = invr()
f = True
c = 0

first, last = -1, -1

for i in range(n-1):
    if arr[i] > arr[i+1]:
        if c == 0:
            first = i+1
        if c > 2:
            print 'no'
            sys.exit()
            break
        if f == True:
            f = False
            c += 1
        if arr[i]-arr[i+1] > 1:
            print 'no'
            sys.exit()
            break
        

    else:
        if f == False:
            last = i+1
            c += 1
            f = True

if last == -1:
    last = n
if first == -1:
    first = 1

if c <= 2 and c > 0:
    print 'yes'
    print str(first) + " " + str(last)
else:
    print 'yes'
    print str(1) + " " + str(1)

        
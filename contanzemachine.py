
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


arr = insr()

#parse for areas of interest

counter = 0
cur = ''

if arr[0] == 'm' or arr[0] == 'w':
    print 0
    sys.exit()


dp_old = 1
dp_new = 1

for i in range(1, len(arr)):
    if arr[i] == 'm' or arr[i] == 'w':
        print 0
        sys.exit()
    if arr[i] == 'u' and arr[i-1] == 'u':
        dp_new, dp_old = dp_old + dp_new, dp_new
    elif arr[i] == 'n' and arr[i-1] == 'n':
        dp_new, dp_old = dp_old + dp_new, dp_new
    else:
        dp_old = dp_new

print dp_new%(10**9+7)



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


# r = raw_input()

n, k = invr()
arr = invr()

mx = n

d = defaultdict(int)
d2 = defaultdict(int)

for i, a in enumerate(arr):
    d[i+1] = a
    d2[a] = i+1
    if a == n:
        ind_start = i

left_students = {i:i for i in range(1, n+1)}

c,w = 0,0
ans = [0]*n


while w < n:
    left = max(0, ind_start - k)
    right = min(n-1, ind_start + k)

    for i in range(left, right+1):
        if arr[i] != -1:
            arr[i] = -1
            d[arr[i]] = -1
            w += 1
            if c % 2 == 0:
                ans[i] = '1'
            else:
                ans[i] = '2'

    c += 1
    ind_start = d2[max(arr)]-1
    
print ''.join([str(a) for a in ans])
        
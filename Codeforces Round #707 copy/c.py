
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque, defaultdict
from copy import deepcopy as dc

# sys.setrecursionlimit(10**6)


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

n = inp()
arr = invr()

d = {}

for i in range(n):
    for j in range(i):
        s = arr[i] + arr[j]

        if s in d:
            if len(set([i+1, j+1, d[s][0]+1, d[s][1]+1])) == 4:
                print 'YES'
                print i+1, j+1, d[s][0]+1, d[s][1]+1
                sys.exit()
            else:
                continue
        else:
            d[s] = (i, j)

print 'NO'
        

-
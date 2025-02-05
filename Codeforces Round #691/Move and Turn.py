
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

"""
assuming that n is even, n%2==0:
we make n//2 moves horizontally and n//2 moves vertically
and these moves can be thought of as independent.

if n = 10, we make 5 moves left-right and 5 moves up-down.
when making 5 up-down moves, we can end up in 6 positions, we can choose 0up5down, ...., 5up0down.
same with left right, so we get 6*6

if n is odd e..g n = 11, we can get 6 updown and 5 leftright or 6 leftright and 5 updown.
we cannot end in the same positions in both approaches since parity.
so we have 6*7 times 2 there

e.g.
for n = 3:
    2 * (2) * (3) = 6

"""

n = inp()

if n % 2 == 0:
    ans = (n//2 + 1)**2
else:
    ans = 2 * ((n+1)//2) * ((n+1)//2 + 1)

print ans
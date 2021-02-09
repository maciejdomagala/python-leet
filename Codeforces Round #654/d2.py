
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

n = inp()
arr = invr()

a,b = [-1],[-1]

seq = 0

for i in range(0, n, 2):
    f = False
    x = arr[i]
    y = arr[i+1]

    if x == a[-1]:
        a.append(x)
        f = True
    elif x == b[-1]:
        b.append(x)
        f = True

    if y == a[-1]:
        a.append(y)
        f = True
    elif y == b[-1]:
        b.append(y)
        f = True

    if f == False:
        a.append(x)
        a.append(y)
    



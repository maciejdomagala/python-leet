
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
    k, p1 = invr()
    colors_now = invr()
    colors_later = invr()
    painters = invr()
    ans = []
    f = False

    dem, demi =[], []
    for i, (a,b) in enumerate(zip(colors_now, colors_later)):
        if a != b:
            dem.append(b)
            demi.append(i)

    for i,a in enumerate(dem):
        if a == painters[-1]:
            last_color = demi[i]
            f = True
            break

    if f == False:
        for i, a in enumerate(colors_later):
            if a == painters[-1]:
                last_color = i
                break
        else:
            print 'NO'
            continue

    ans=[]

    for p in painters[::-1]:
        for i, a in enumerate(dem):
            if a == p:
                ans.append(demi[i])
                dem.pop(i)
                demi.pop(i)
                break
        else:
            ans.append(last_color)

    if len(dem) == 0:
        print 'YES'
        print ' '.join([str(a+1) for a in ans[::-1]])
    else:
        print 'NO'
    

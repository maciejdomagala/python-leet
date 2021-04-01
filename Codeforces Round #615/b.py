
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
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

def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd


# r = raw_input()

for _ in range(inp()):
    n = inp()
    points = []
    f = True

    for _ in range(n):
        x, y = invr()
        p = (x,y)

        points.append(p)

    points = sorted(points, key= lambda x: (x[0], x[1]))
    points.insert(0, (0,0))
 
    dist = []

    for i in range(1, n+1):
        if points[i][1] < points[i-1][1]:
            f = False
            break
        else:
            right = (points[i][0]-points[i-1][0])
            up = (points[i][1]-points[i-1][1])
            
            dist.append('R'*right)
            dist.append('U'*up)

    if f:
        print 'YES'
        print ''.join(dist)
    else:
        print 'NO'
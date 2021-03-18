
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

for _ in range(inp()):
    n = inp()
    arr = invr()

    minodd, mineven = arr[1], arr[0]
    minans = n*minodd + n*mineven
    ansevens, ansodd = n*mineven,n*minodd


    odds, evens = [],[]
    sumevens, sumodds =0,0
    cevens, codds = 0,0
    for i, a in enumerate(arr[2:]):
        if i % 2 == 0:
            if a < mineven:
                sumevens += mineven
                cevens += 1
                mineven = a
            else:
                cevens += 1
                sumevens += a

            ansevens = mineven*((n-cevens)) + sumevens

        if i % 2 == 1:
            if a < minodd:
                sumodds += minodd
                codds += 1
                minodd = a
            else:
                codds += 1
                sumodds += a

            ansodd = minodd*((n-codds)) + sumodds

        # print ansevens
        # print ansodd
            
        ans = ansodd + ansevens
        if ans < minans:
            minans = ans

    print minans

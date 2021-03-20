
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
    n, a, b = invr()
    arr = insr()
    inf = float('inf')

    dp = [[inf]*2 for _ in range(n)]

    dp[0][0] = b
    dp[0][1] = inf

    for i in range(1, n):
        if arr[i] == '1':
            dp[i][1] = min(dp[i-1][0]+2*a+2*b, dp[i-1][1]+a+2*b)
            dp[i][0] = inf
        if arr[i] == '0':
            if arr[i-1] == '0':
                dp[i][1] = min(dp[i-1][1]+a +2*b, dp[i-1][0]+2*a+2*b)
                dp[i][0] = min(dp[i-1][1]+2*a+b, dp[i-1][0]+a+b)
            else:
                dp[i][1] = min(dp[i-1][1]+a +2*b, dp[i-1][0]+2*a+2*b)
                dp[i][0] = inf

    print min(dp[n-1][1]+2*a+b, dp[n-1][0]+a+b)

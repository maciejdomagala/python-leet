
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


n = inp()
arr = invr()

inf = 10**8
dp = [[10**8]*3 for _ in range(n)]

#0 - rest
#1 - contest
#2 - gym

dp[0][0] = 1

if arr[0] == 1 or arr[0] == 3:
    dp[0][1] = 0

if arr[0] == 2 or arr[0] == 3:
    dp[0][2] = 0

for i in range(1, n):
    a = arr[i]
    dp[i][0] = 1 + min(dp[i-1][0],dp[i-1][1], dp[i-1][2])

    if a == 1 or a == 3:
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])

    if a == 2 or a == 3:
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])

print min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
        
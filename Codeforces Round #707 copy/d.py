
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque
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


r = raw_input()

n = inp()
a = invr()

dp = [[0,0] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 1
dp[1][1] = 1

if a[1] > a[0]:
    dp[1][0] = 2

for i in range(2, n):

    if a[i] > a[i-1]:
        dp[i][0] = dp[i-1][0]
    else:
        dp[i][0] = 1

    if a[i] <= a[i-1]:
        if a[i] > a[i-2]:
            dp[i][1] = max(dp[i-2][0]+1, dp[i-1][1] + 1)
        else:
            dp[i][1] = dp[i-1][1] + 1
    else:
        dp[i][1] = 1

print dp




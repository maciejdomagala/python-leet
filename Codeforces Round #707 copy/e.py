
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


# r = raw_input()

for _ in range(inp()):
    n = inp()
    arr = invr()

    ans_small = [0]*n
    ans_big = [0]*n

    ans_small[0] = arr[0]
    ans_big[0] = arr[0]

    small, big = deque([]), deque([])

    for i in range(1, arr[0]):
        small.append(i)
        big.append(i)

    cur = arr[0]

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            ans_small[i] = arr[i]
            ans_big[i] = arr[i]

            for i in range(cur+1, arr[i]):
                small.append(i)
                big.append(i)

            cur = arr[i]

        else:
            ans_small[i] = small.popleft()
            ans_big[i] = big.pop()

    print ' '.join([str(a) for a in ans_small])
    print ' '.join([str(a) for a in ans_big])




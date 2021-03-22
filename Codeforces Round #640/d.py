
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
from copy import deepcopy as dc
from collections import defaultdict


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
        
# a = raw_input()

for _ in range(inp()):

    n = inp()

    arr = invr()
    a, b = 0,0
    last_alice, last_bob = 0,0

    if n == 1:
        if arr[0] == 0:
            print 0, 0, 0
            continue
        else:
            print 1, arr[0], 0
            continue

    f = True

    i = 0
    j = n-1
    counter = 0
    while i < j:
        last_alice = 0
        counter += 1
        while last_alice <= last_bob:
            a += arr[i]
            last_alice += arr[i]
            i += 1
            if i > j:
                f = False
                break
        if f == False:
            break
        last_bob = 0
        counter += 1
        while last_bob <= last_alice:
            last_bob += arr[j]
            b += arr[j]
            j -= 1
            if j < i:
                f = False
                break
        if f == False:
            break
        

    print counter, a , b
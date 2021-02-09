
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
# arr = invr()


l = invr()

# length = random.randint(7, 10)

# l = [random.randint(0, 2) for _ in range(length)]
# print(l)
l1 = [l.pop(0)]
l2 = []

res=1
for x in l:
    if x == l1[-1]:
        try:
            if x != l2[-1]:
                res += 1
        except IndexError:
            res+=1
        l2.append(x)

    else:
        l1.append(x)
        res += 1

print res
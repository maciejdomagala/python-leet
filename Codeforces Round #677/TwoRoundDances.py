import sys
input = sys.stdin.readline
import math
from math import sqrt
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

ans = binomial(n, n//2) // 2
ans *= math.factorial(n//2 - 1) ** 2

print ans

"""
so if we have n people, we choose half of them - other half will be fixed.
we can do that in a binomial number of way, meaning (n  n//2) binomial.
we want to use combinations without duplicates. so once a pair (a_i, a_j) is taken it is not counted as (a_j, a_i) also.

if we are taking k people from group of n people (here k will actually be n//2) we do it as n!/((n-k)!*k!). then we have to halve the 
number, cause we have two dances and these are not ordered.

then inside of the single round dance, we can order dancers in (n//2 - 1)! ways. (fixing first dancer and the rest is arbitrary.)

and we need to multiply the number of these setups in two round dances, so essentially that would be (n//2 - 1)! ** 2 ways times the previous value.
"""
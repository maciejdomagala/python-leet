
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

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

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

a, b = invr()

if b > 9*a:
    print str(-1) + " " + str(-1)
    sys.exit()

if b == 0:
    if a != 1:
        print str(-1) + " " + str(-1)
        sys.exit()
    else:
        print str(0) + " " + str(0)
        sys.exit()

div = b // 9
mod = b % 9

if mod != 0:
    s = '9'*div + str(mod)
    mx = s + (a-len(s))*'0'
else:
    s = '9'*div
    mx = s + (a-len(s))*'0'


###for min
if mod == 0:
    if a == 1:
        s = '9'
    elif a == 2:
        s = '18'
    else:
        s = '1' + (a-2)*'0' + '8'
elif div == a:
    s = '9'*div
elif div == a-1:
    s = str(mod) + '9'*div
else:
    s = str(mod-1) + div*'9'
    s = '1' + '0'*(a-1-len(s)) + s

print s + " " + mx

# a, b = invr()

# if b > 9*a:
#     print str(-1) + " " + str(-1)
#     sys.exit()

# if b == 0:
#     if a != 1:
#         print str(-1) + " " + str(-1)
#         sys.exit()
#     else:
#         print str(0) + " " + str(0)
#         sys.exit()

# ###for max:
# div = b // 9
# mod = b % 9

# if mod != 0:
#     s = '9'*div + str(mod)
#     mx = s + (a-len(s))*'0'
# else:
#     s = '9'*div
#     mx = s + (a-len(s))*'0'

# ###for min
# if div == a:
#     s = '9'*div
# elif div == a-1:
#     s = str(mod) + '9'*div
# else:
#     s = str(mod-1) + div*'9'
#     s = '1' + '0'*(a-1-len(s)) + s

# print s + " " + mx
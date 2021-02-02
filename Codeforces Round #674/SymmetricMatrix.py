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

for _ in range(inp()):
    n, m = invr()
    f2 = True
    if m % 2 == 1:
        f2 = False

    f = False

    for _ in range(n):
        a, b = invr()
        c, d = invr()

        if b == c:
            f = True
    
    if f2 == False:
        print "NO"
    elif f == True:
        print "YES"
    else:
        print "NO"

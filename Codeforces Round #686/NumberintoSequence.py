import sys
input = sys.stdin.readline
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

for _ in range(inp()):
    n = inp()

    f=prime_factorization(n)
    ca=Counter(f)
    c=ca.most_common()[0]
    ans=[c[0]]*(c[1]-1)

    for i in ans:
        n = n//i

    ans.append(n)

    print len(ans)
    print ' '.join([str(a) for a in ans])
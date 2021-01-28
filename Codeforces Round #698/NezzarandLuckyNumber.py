import sys
input = sys.stdin.readline

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

for _ in range(inp()):
    n, q = invr()

    nums = invr()
    for num in nums:
        f = False
        i = 0
        while num > 0 and i < q:
            if num % q == 0:
                f = True
                break

            if str(q) in str(num):
                f = True
                break

            num -= q

        if f == True:
            print('YES')
        else:
            print('NO')

    



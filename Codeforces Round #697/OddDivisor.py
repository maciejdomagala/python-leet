import sys
input = sys.stdin.readline

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

#bit counting:

# for _ in range(inp()):
#     n = inp()

#     if bin(n)[2:].count('1') == 1:
#         print 'NO'
#     else:
#         print 'YES'


for _ in range(inp()):
    n = inp()

    if n&(n-1) == 0:
        print 'NO'
    else:
        print 'YES'


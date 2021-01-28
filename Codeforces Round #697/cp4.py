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

n = inp()

for i in range(n):
    n,m = invr()

    a = invr()
    b = invr()


    pairs = [(i,j) for i,j in zip(a, b)]
    pairs = sorted(pairs, key= lambda x: (x[1], -x[0]))


    points, imp = 0,0
    ind = 0

    while points < m and ind < len(pairs):
        points += pairs[ind][0]
        imp += pairs[ind][1]
        ind += 1

    if points < m:
        print(-1)
        sys.exit()

    diff = points - m

    subarr = pairs[1:ind][::-1]

    for j in range(len(subarr)):
        if subarr[j][0] < diff:
            diff -= subarr[j][0]
            imp -= subarr[j][1]

    print(imp)

    
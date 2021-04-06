
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, deque, defaultdict
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

def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd

#### BFS ALGORITHM
def bfs(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:            
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level, parent

#### BFS FOR SHORTEST PATH
def bfs2(n, m):
    vis = set()
    que = deque([n])
    dep = defaultdict(int)
    dep[n] = 0

    while True:
        while que:
            el = que.popleft()
            vis.add(el)

            if el == m:
                print dep[el]
                return

            if el-1 not in vis and el-1 > 0:
                que.append(el-1)
                dep[el-1] = dep[el] + 1
            if 2*el not in vis and 2*el < 2*m:
                que.append(2*el)
                dep[2*el] = dep[el] + 1

#for binary tree
class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data

#for graphs

a, b = invr()
arr = invr()

i = 0
while i <= b:
    if i == b:
        print 'YES'
        sys.exit()

    i += arr[i-1]

print 'NO'
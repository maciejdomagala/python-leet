
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


arr = [-1]*10
arr[0] = 0
arr[1] = 1
arr[2] = 5
arr[5] = 2
arr[8] = 8


def check_time(time, arr=arr):

    for i in time:
        if arr[int(i)] == -1:
            return -1
    else:
        hour = str(arr[int(time[3])]) + str(arr[int(time[2])])
        minute = str(arr[int(time[1])]) + str(arr[int(time[0])])
        return (hour, minute)



for _ in range(inp()):

    h, m = invr()
    f = False

    s = insr()

    time = s[0]+s[1]+s[3]+s[4]

    while str(time) != '9999':
        time = str(time)
        if len(time) < 4:
            time = '0'*(4-len(time)) + time
        if check_time(time) == -1:
            time = int(time) + 1
        else:
            if int(check_time(time)[0]) < h and int(check_time(time)[1]) < m:
                if int(time[:2]) < h and int(time[2:4]) < m:
                    print time[:2]+ ":" + time[2:4]
                    f = True
                    break
                else:
                    time = int(time) + 1
            else:
                time = int(time) + 1

    if f == False:
        print '00:00'






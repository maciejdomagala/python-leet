# Codeforces Round \#614

A. ConneR and the A.R.C. Markland-N

n is too big here to iterate through all floors, but k \(number of closed floors\) is &lt;= 1000.  
hence, we only need to check floors between s-1000 and s+1000. 

```python
for _ in range(inp()):
    n, s, k = invr()
    arr = invr()
    sett = set(arr)
    mn1, mn2 = float('inf'), float('inf')
    i = 0

    while s+i <= n and i < 1002:
        if s+i not in sett:
            mn1 = i
            break
        i += 1
    i = 0

    while i < s and i < 1002:
        if s-i not in sett:
            mn2 = i
            break
        i += 1
    
    
    print min(mn1, mn2) 
```

B. JOE is on TV!

Best case is when contestants go off one by one.

```python
n = inp()
ans= 0

for i in range(1,n+1):
    ans += 1/i

print ans
```

C. NEKO's Maze Game

```python
lava = 0
n, q = invr()
s = set()
for _ in range(q):
    x, y = invr()
    p = (x, y)

    for i in range(y-1, y+2):
        if x == 1:
            h = 2
        else:
            h = 1
        w = (h, i)
        if w in s:
            if p in s:
                lava -= 1
            else:
                lava += 1
            
    if p in s:
        s.remove(p)
    else:
        s.add(p)

    if lava > 0:
        print 'No'
    else:
        print 'Yes'
```


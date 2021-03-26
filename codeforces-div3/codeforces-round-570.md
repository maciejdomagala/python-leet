# Codeforces Round \#570

A. Nearest Interesting Number

```python
n = inp()

while sum([int(a) for a in str(n)]) % 4 != 0:
    n += 1

print n
```

B. Equalize Prices

```python
for _ in range(inp()):
    n, k = invr()

    arr = invr()

    mn, mx = min(arr), max(arr)

    if mn+k < mx-k:
        print -1
    else:
        print mn+k
```

C. Computer Game

Here we simply calculate the number of games with charging the battery we can perform. If we have any spare energy, we check if it's enough to swap the game with battery to the game without battery charging. We are doing it as many times as it is possible. When it's not possible anymore, we return the value.

```python
for _ in range(inp()):

    k,n,a,b = invr()

    if n*b >= k:
        print -1
        continue

    diff = a-b

    res = k-n*b

    turns = res//diff
    if res % diff == 0:
        turns -= 1

    print min(turns, n)
```

D. Candy Box \(easy version\)

We are using Counter the get the numbers of candies of the given type. We sort the array in descending order and go through it.

```python
for _ in range(inp()):

    n = inp()
    arr = invr()

    ca = Counter(arr)

    zz = sorted(ca.values(), reverse=True)

    mn = zz[0]
    i = 0
    c = 0

    while i < len(zz):
        if mn == 0:
            break
        if zz[i] >= mn:
            c += mn
            mn -= 1
        else:
            mn = zz[i]
            c += mn

        i += 1

    print c
```


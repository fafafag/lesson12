def sieve(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    b.reverse()
    b = tuple(b)
    return b

a = [15, 2, 9, 2, 1, -3, 15, 31, 2]
print(sieve(a))
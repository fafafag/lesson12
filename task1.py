def tpl_sort(a):
    b = []
    for i in range(len(a)):
        if type(a[i]) != int:
            return a
        b.append(a[i])
    b.sort()
    b = tuple(b)
    return b

# a = (15, 2, 9, 54, 1, -3, 31, -26, "d")
a = (15, 2, 9, 54, 1, -3, 31, -26)
print(tpl_sort(a))


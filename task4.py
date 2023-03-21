def del_from_tuple(a, e):
    if a.count(e) == 0:
        return a
    a = list(a)
    del a[a.index(e)]
    a = tuple(a)
    return a

print("Введите последовательность чисел :")
a = [int(i) for i in input().split()]
a = tuple(a)

print("Введите элемент :")
e = int(input())

print (del_from_tuple(a, e))
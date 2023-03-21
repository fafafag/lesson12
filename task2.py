def slicer(kortezh, random_element):
    n = tuple()
    m = (kortezh.count(random_element))
    if m == 0:
        return n
    elif m == 1:
        return kortezh[kortezh.index(random_element):]
    elif m > 1:
        f_index = kortezh.index(random_element)
        s_index = kortezh.index(random_element, f_index + 1) + 1
        return kortezh[f_index:s_index]


print("Введите последовательность чисел: ")
a = [int(i) for i in input().split()]
kortezh = tuple(a)

print("Введите элемент: ")
random_element = int(input())
print(slicer(kortezh, random_element))
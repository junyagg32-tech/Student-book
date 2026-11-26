import random

list1 = [random.randint(-10, 10) for i in range(7)]
list2 = [random.randint(-10, 10) for i in range(7)]

print(list1, list2)

def darts1():
    list3 = [list1 + list2]

    print(list3)


def darts2():
    list3 = []
    for i in list1:
        if i not in list3:
            list3.append(i)

    for i in list2:
        if i not in list3:
            list3.append(i)

    print(list3)

def darts3():
    list3 = []

    for i in list2:
        if i in list1 and i not in list3:
            list3.append(i)

    print(list3)

def darts4():
    list3 = []

    for i in list1:
        if i not in list2 and i not in list3:
            list3.append(i)
    for i in list2:
        if i not in list1 and i not in list3:
            list3.append(i)
    print(list3)

def darts5():
    list3 = [min(list1), max(list1), min(list2), max(list2)]

    print(list3)
darts5()
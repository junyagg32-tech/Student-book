# Задание 1
import random

def cik():
    sick = []
    for i in range(15):
        sick.append(random.randint(-10,10))
    print("список", sick)

    sumneg = 0
    sum2 = 0
    sum1 = 0
    in3 = 1

    for i in range(len(sick)):
        if sick[i] < 0:
            sumneg += sick[i]
        if sick[i] % 2 == 0:
            sum2 += sick[i]
        if sick[i] % 2 != 0:
            sum1 += sick[i]
        if i % 3 == 0:
            in3 *= sick[i]

    mins = sick.index(min(sick))
    mans = sick.index(max(sick))
    ind = 1

    if mins > mans:
        mins, mans = mans, mins
    for i in range(mins, mans):
        ind *= sick[i]

    frst = None
    last = None

    for i in range(len(sick)):
        if sick[i] > 0:
            if frst is None:
                frst = i
            last = i

    sumf = 0
    if frst is not None and last is not None:
        if last > frst:
            frst, last = last, frst
        for i in range(frst, last):
            sumf += sick[i]
    else:
        sumf = 0


    print(sumneg, sum2, sum1, ind, sumf, in3)
def cik2():
    sss = []
    for i in range(15):
        sss.append(random.randint(-10,10))
    print("основной список -", sss)

    ss1 = []
    cd = 0
    for i in range(len(sss)):
        if sss[i] % 2 == 0:
            ss1.append(sss[i])

    print(f"список целых чётных чисел {ss1}")

    ss2 = []
    for i in range(len(sss)):
        if sss[i] % 2 != 0:
            ss2.append(sss[i])
    print(f"список целых нечётных чисел {ss2}")

    ss3 = []
    for i in range(len(sss)):
        if sss[i] < 0:
            ss3.append(sss[i])

    print(f"список целых отрицательных чисел {ss3}")

    ss4 = []
    for i in range(len(sss)):
        if sss[i] > 0:
            ss4.append(sss[i])

    print(f"список целых положительных чисел {ss4}")


cik2()


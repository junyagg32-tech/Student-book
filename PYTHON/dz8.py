# задание 1
def ex1():

    a = int(input("введите начало диапозона: "))
    b = int(input("введите конец диапозона: "))

    if a > b:
        a, b = b, a

    coc = 0
    suma1 = 0

    for ch in range(a, b + 1):
        if ch % 2 == 0:
            coc += 1
            suma1 += ch

    print("сумма чётных чисел =", suma1)

    suma2 = 0
    coc1 = 0
    for nch in range(a, b + 1):
        if nch % 2 != 0:
            coc1 += 1
            suma2 += nch

    print("сумма не чётных чисел =", suma2)

    suma3 = 0
    coc3 = 0
    for nine in range(a, b + 1):
        if nine % 9 == 0:
            coc3 += 1
            suma3 += nine

        print("сумма чисел кратных 9 = ", suma3)

    if coc == 0:
        print("среднее арифмитическое чётных чисел = 0" )
    else:
        print("среднее арифмитическое чётных чисел =", suma1 / coc )
    if coc1 == 0:
        print("среднее арифмитическое не чётных чисел = 0" )
    else:
        print("среднее арифмитическое не чётных чисел =", suma2 / coc1 )
    if coc3 == 0:
        print("среднее арифмитическое чисел кратных 9 = 0" )
    else:
         print("среднее арифмитическое чисел кратных 9 =", suma3 / coc3 )
# Задание 2
def ex2():
    c = int(input("введите количество символов: "))
    d = input("введите желаемый символ: ")

    if c < 0:
        c *= -1

    while c > 0:
            print(d)
            c -= 1

# Задание 3
def ex3():
    while True:
        e = int(input("введите любое число: "))
        if e == 7:
            print("good bye!!! ^_^")
            break
        elif e > 0:
            print("number is positive")
        elif e == 0:
            print("number is equal to zero")
        else:
            print("number is negative")

# Задание 4
def ex4():
    suma = 0
    man = None
    minu = None
    while True:
        f = int(input("введите любое число: "))
        if f == 7:
            print("good bye!!! ^_^")
            break
        else:
            suma += f
            if man is None:
                man = f
                minu = f
            else:
                if f > man:
                    man = f
                if f < minu:
                    minu = f
        print(f"сумма чисел = {suma}. Максимальное = {man} а минимальное = {minu}")
ex4()





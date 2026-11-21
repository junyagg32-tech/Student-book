# Задание 1

def ex1():

    while True:
        try:
            x = int(input("введите число 1: "))
            print(x ** 2)
            break
        except ValueError:
            print("Пожалуйста введите целое число.")



# Задание 2

def ex2():

    while True:
        try:
            x = int(input("введите число 1: "))
            y = int(input("введите число 2: "))
            print(x / y)
            break
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except ValueError:
            print("Пожалуйста введите два целых числа.")

# Задание 3

def ex3():
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    while True:
        try:
            index = int(input("введите желаемый день недели от 1 до 7: "))
            if index <= 0:
                raise IndexError

            print(days[index - 1])
            break
        except IndexError:
            print("такого дня нет. введите день недели.")

ex1()
ex2()
ex3()








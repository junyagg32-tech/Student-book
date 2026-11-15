# Задание 1
day1 = 'Понедельник'
day2 = 'Вторник'
day3 = 'Среда'
day4 = 'Четверг'
day5 = 'Пятница'
day6 = 'Суббота'
day7 = 'Воскресенье'

day0 = int(input("Введите номер от 1 до 7: "))

if day0 == 1:
    print(day1)
elif day0 == 2:
    print(day2)
elif day0 == 3:
    print(day3)
elif day0 == 4:
    print(day4)
elif  day0 == 5:
    print(day5)
elif day0 == 6:
    print(day6)
elif day0 == 7:
    print(day7)
else:
    print("Выбрано неверное число")


# Задание 2
mounth1 = "Январь"
mounth2 = "Февраль"
mounth3 = "Март"
mounth4 = "Апрель"
mounth5 = "май"
mounth6 = "Июнь"
mounth7 = "Июль"
mounth8 = "Август"
mounth9 = "Сентябрь"
mounth10 = "Октябрь"
mounth11 = "Ноябрь"
mounth12 = "Декабрь"

moun = int(input("Введите номер от 1 до 12: "))

if moun == 1:
    print(mounth1)
elif moun == 2:
    print(mounth2)
elif moun == 3:
    print(mounth3)
elif moun == 4:
    print(mounth4)
elif moun == 5:
    print(mounth5)
elif moun == 6:
    print(mounth6)
elif moun == 7:
    print(mounth7)
elif moun == 8:
    print(mounth8)
elif moun == 9:
    print(mounth9)
elif moun == 10:
    print(mounth10)
elif moun == 11:
    print(mounth11)
elif moun == 12:
     print(mounth12)
else:
    print("Выбрано невероне число")

# Задание 3

nume = float(input("Введите любое число"))

if nume >= 1:
    print("Number is positive")
elif nume == 0:
    print("Number is equal to zero")
else:
    print("Number is negative")


# Задание 4

Num1 = int(input("введите число 1: "))
Num2 = int(input("введите число 2: "))

if Num1 == Num2:
    print("числа равны")
elif Num1 > Num2:
    print(Num1, Num2)
else:
    print(Num2, Num1)
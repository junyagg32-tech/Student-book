
print("Задание 1")
num = float(input("Введите число: "))

if num > 0:
    print("Положительное")
elif num < 0:
    print("Отрицательное")
else:
    print(num)

print("Задание 2")
num1 = int(input("Введите число:"))

if num1 % 2 == 0:
    print("Чёт")
else:
    print("Нечёт")

print("Задание 3")

a = float(input("Введите число 1:"))
b = float(input("Введите число 2:"))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("они равны")

print("Задание 4")

ad = float(input("Введите число 1: "))
bd = float(input("Введите число 2: "))
cd = float(input("Введите число 3: "))

if ad >= bd and ad >= cd:
    print(ad)
elif bd >= ad and bd >= cd:
    print(bd)
else:
    print(cd)


print("Задание 5")

ac = float(input("Введите первое число: "))
bc = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    print(ac + bc)
elif op == "-":
    print(ac - bc)
elif op == "*":
    print(ac * bc)
elif op == "/":
    if bc == 0:
        print("Ошибка незя на нуль делить!")
    else:
        print(ac / bc)
else:
    print("попробуй снова")

print("Задание 6")

year = int(input("Введите год:"))

if (year % 400 == 0):
    print("Високосный год")
else:
    print("Обычный год")

print("Задание 7")

af = float(input("Сторона a: "))
bf = float(input("Сторона b: "))
cf = float(input("Сторона c: "))

if af + bf > cf and af + cf > bf and bf + cf > af:
    print("Треугольник существует.")
else:
    print("не существует")

print("Задание 8")

sco = int(input("Введите количество баллов (0–100):"))

if sco >= 90 and sco <= 100:
    print("Отлично")
elif sco >= 75 and sco <= 89:
    print("Хорошо")
elif sco >= 60 and sco <= 74:
    print("Удовлетворительно")
elif sco >= 0 and sco <= 59:
    print("Неудовлетворительно")
else:
    print("Ошибка оно больше или меньше 100")

print("Задание 9")
base = 500
discount = 0

age = int(input("Введите возраст: "))
day = int(input("Введите день недели (1–7): "))

if age < 12:
    discount = discount + 50
elif age >= 65:
    discount = discount + 30

if day == 6 or day == 7:
    discount = discount - 20

final = base * (100 - discount) / 100
print("Итого", final)

password = input("Введите пароль: ")
is_valid = True

if len(password) < 8:
    print("Ошибка: длина пароля должна быть не менее 8 символов.")
    is_valid = False

if is_valid:
    print("Поздравляем! Пароль надёжный.")
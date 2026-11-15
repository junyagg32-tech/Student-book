# Задание 1
from unittest import skip

Fin = int(input("Введите число 1"))
Fin2 = int(input("Введите число 2"))

for hom in range(Fin, Fin2 + 1):
    if hom % 7 == 0:
        print(hom)


# Задание 2
ass = int(input("Введите начало диапозона"))
asus = int(input("Введите конец диапозона"))

print("все числа")
for i in range(ass, asus + 1):
    print(i)



print("Все числа в убывающем порядке")
for i in range(asus, ass - 1, -1):
     print(i)

coc = 0
print("Все числа кратные 7")
for i in range(ass, asus + 1):
    if i % 7 == 0:
        print(i)
        coc += 1
if coc == 0:
    print(coc)

coc = 0
print("количество числел кратных 5")
for i in range(ass, asus + 1):
    if i % 5 == 0:
        coc += 1
print(coc)

# Задание 3
a = int(input("Введите начало диапозона"))
b = int(input("Введите конец диапозона"))

for i in range(a, b + 1):
    if i % 3 == 0:
        print("fizz", end=" ")
    elif i % 5 == 0:
        print("buzz", end=" ")
    elif i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz", end=" ")
    else:
        print(i, end=" ")



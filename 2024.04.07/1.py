name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = int(input("Введите год рождения: "))
print(surname, name + ",", 2024 - year)


# с использованием библиотеки time

import time

print("с использованием библиотеки time")
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = int(input("Введите год рождения: "))
print(surname, name + ",", time.localtime().tm_year - year)


# Введите имя: Дарья
# Введите фамилию: Курсанова
# Введите год рождения: 2000
# Курсанова Дарья, 24
# с использованием библиотеки time
# Введите имя: Дарья
# Введите фамилию: Курсанова
# Введите год рождения: 2000
# Курсанова Дарья, 24
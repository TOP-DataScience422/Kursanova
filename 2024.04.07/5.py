integer = input("Введите целую часть числа миль: ")
fraction = input("Введите дробную часть числа миль: ")
# ИСПОЛЬЗОВАТЬ: PEP 8 рекомендует для имён переменных использовать змеиный_нижний_регистр (lower_snake_case)
value_millis = float(integer + "." + fraction)
value_km = value_millis * 1.61

# print(f'{value_millis} миль = {round(value_km,1)} км')
# ИСПОЛЬЗОВАТЬ: в f-строках вам не нужна функция round()
print(f'{value_millis} миль = {value_km:.1f} км')

# Введите целую часть числа миль: 13
# Введите дробную часть числа миль: 5
# 13.5 миль = 21.7 км


# ИТОГ: очень хорошо — 4/4


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

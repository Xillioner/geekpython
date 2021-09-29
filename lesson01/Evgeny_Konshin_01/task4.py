# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Вычисления
# 2354 % 10
# 4
# 2354 - 4
# 2350
# 2350 / 10

# Проверил на числе 2354 получил 5
# Проверил на числе 12349857659 получил число 9

positive_number = int(input("Введи целое положительное число - "))

max_number = 0

while positive_number != 0:
    remainder = positive_number % 10

    if max_number < remainder:
        max_number = remainder

    positive_number = positive_number - remainder
    positive_number //= 10

print(f"Максимальное число: {max_number}")

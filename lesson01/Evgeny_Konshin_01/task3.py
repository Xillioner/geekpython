# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Проверил на 3, получил 369

count = 0
result = 0
limit_number = 3
con_string = ""

number_n = input("Введите число: ")

while count < limit_number:
    con_string = f"{con_string}{number_n}"
    result += int(con_string)
    count += 1

print(f"Результат: {result}")

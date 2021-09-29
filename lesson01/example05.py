stop_count = int(input("Введи конечное число: "))
delimiter = int(input("Введи делимое: "))

current_count = 0

while True:
    if current_count == stop_count:
        break

    current_count += 1

    if current_count % delimiter == 0:
        continue
    print(current_count)

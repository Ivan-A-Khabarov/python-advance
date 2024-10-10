while True:
    number = input("Введите число от 1 до 999: ")
    if not number.isdigit() or not 1 <= int(number) <= 999:
        continue
    number = int(number)

    if 0 < number < 10:
        result = number ** 2
        print(f"{number} - это цифра, ее квадрат равен {result}")
    elif 10 <= number < 100:
        first_digit = number // 10
        second_digit = number % 10
        product = first_digit * second_digit
        print(f"{number} - это двузначное число, произведение его цифр равно {product}")
    else:
        reversed_number = int(str(number)[::-1])
        print(f"{number} - это трехзначное число, его зеркальное отображение равно {reversed_number}")
    break
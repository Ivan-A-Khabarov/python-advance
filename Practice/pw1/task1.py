year = int(input("Введите год: "))

if year % 4 != 0:
    print("Не високосный год.")
elif year % 100 == 0 and year % 400 != 0:
    print("Не високосный год.")
else:
    print("Високосный год.")
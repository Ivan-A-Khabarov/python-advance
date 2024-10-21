# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
day_of_week = current_datetime.strftime('%A')
week_number = current_datetime.isocalendar()[1]

print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")

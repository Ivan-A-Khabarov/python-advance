# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import datetime
import logging

LOGGER = logging.getLogger(__name__)


def convert_date_string_to_datetime(date_string):
    """Преобразует строку даты в формат "N-й день недели M месяца" в дату текущего года."""
    try:
        day_of_week, month = date_string.split()
        weekday_number = int(day_of_week[:-2])
        month_number = month[0]

        if month_number in '12345678910':
            month_number -= 1  # Перевод номера месяца в диапазоне 1-12

        year = datetime.date.today().year
        first_day_of_month = datetime.date(year, month_number, 1)
        weekday_number = weekday_number if first_day_of_month.weekday() == ord(
            day_of_week[-1]) else weekday_number % 5 + 1
        date = first_day_of_month + datetime.timedelta(days=(weekday_number - first_day_of_month.weekday()) % 7)

        return date
    except Exception as e:
        LOGGER.error(f"Неверный формат даты: '{date_string}'. Ошибка: {e}")
        return None


if __name__ == "__main__":
    test_cases = [
        ("1-й четверг ноября",),
        ("3-я среда мая",),
        ("5-й понедельник января",),
        ("7-й вторник февраля",),
    ]

    for date_string in test_cases:
        converted_date = convert_date_string_to_datetime(date_string[0])
        if converted_date is not None:
            print(converted_date)
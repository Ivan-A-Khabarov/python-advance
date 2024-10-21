# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.


import datetime
import sys
import argparse


def convert_date_string_to_datetime(date_string):
    """Преобразует строку даты в формат "N-й день недели M месяца" в дату текущего года."""
    try:
        day_of_week, month = date_string.split()
        weekday_number = int(day_of_week[:-2])
        month_number = int(month[0])

        if month_number > 12 or month_number < 1:
            raise ValueError("Некорректный номер месяца")

        year = datetime.date.today().year
        first_day_of_month = datetime.date(year, month_number, 1)
        weekday_number = weekday_number if first_day_of_month.weekday() == ord(
            day_of_week[-1]) else weekday_number % 5 + 1
        date = first_day_of_month + datetime.timedelta(days=(weekday_number - first_day_of_month.weekday()) % 7)

        return date
    except Exception as e:
        print(f"Неверный формат даты: '{date_string}'. Ошибка: {e}")
        return None


def get_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("date_string", help="Формат: N-й день недели M месяца")
    parser.add_argument("--day", default=datetime.datetime.today().weekday(), type=int, choices=[0, 1, 2, 3, 4],
                        help="День недели (0 - понедельник, ...)")
    parser.add_argument("--month", default=datetime.datetime.today().month, type=int, help="Месяц (от 1 до 12)")
    parser.add_argument("--year", default=datetime.datetime.today().year, type=int, help="Год")

    args = parser.parse_args()

    date_string = args.date_string
    day = args.day
    month = args.month
    year = args.year

    if not date_string:
        print("Параметр 'date_string' не задан. Берём первый день недели.")
        date_string = f"1-й {['monday', 'tuesday', 'wednesday', 'thursday', 'friday'][day]} {month}"

    if not month:
        print("Параметр 'month' не задан. Берём текущий месяц.")
        month = datetime.datetime.today().strftime("%m")

    if not year:
        print("Параметр 'year' не задан. Берём текущий год.")
        year = datetime.datetime.today().year

    return date_string, day, month, year


if __name__ == "__main__":
    date_string, day, month, year = get_command_line_arguments()
    converted_date = convert_date_string_to_datetime(date_string)
    if converted_date is not None:
        print(converted_date.strftime("%Y-%m-%d"))
# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь

def all_companies_profitable(companies):
    # Проходим по каждой компании в словаре
    for name, finances in companies.items():
        # Рассчитываем итоговую прибыль/убыток как сумму всех значений
        profit = sum(finances)

        # Если хотя бы одна компания убыточна (прибыль меньше 0)
        if profit < 0:
            return False

    # Если все компании прибыльные
    return True


# Пример использования функции
companies = {
    "Компания А": [100000, -50000, 30000],
    "Компания Б": [150000, -70000, 20000],
    "Компания В": [50000, -60000, -10000]
}

result = all_companies_profitable(companies)
print(result)

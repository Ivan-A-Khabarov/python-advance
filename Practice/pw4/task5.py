# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def calculate_bonus(names, rates, bonus):
    result = {}
    for name, rate, bonus in zip(names, rates, bonus):
        bonus_percent = float(bonus.strip('%')) / 100
        bonus_amount = rate * bonus_percent
        result[name] = bonus_amount
    result[name] = bonus_amount
    return result

names = ['Иван', 'Петр', 'Сидор']
rates = [10, 20, 30]
bonus = ['10%', '20%', '30%']
result = calculate_bonus(names, rates, bonus)
print(result)

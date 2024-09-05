# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку. С помощью генератора, выведите таблицу.

LOW_LIMIT = 2
UPPER_LIMIT = 10
COLUMNS = 4

# print()
# for seed_first_num in (LOW_LIMIT, LOW_LIMIT + COLUMNS):
#     for second_num in range(LOW_LIMIT, UPPER_LIMIT + 1):
#         for first_num in range(seed_first_num, seed_first_num + COLUMNS):
#             print(f"{first_num: > 2} x {second_num: > 2} = {(first_num * second_num): > 2}", end="\t")
#         print()
#     print()

table = (
    f"{first_num: > 2} x {second_num: > 2} = {(first_num * second_num): > 2}\t" if first_num != seed_first_num + COLUMNS - 1
    else f"{first_num: > 2} x {second_num: > 2} = {(first_num * second_num): > 2}\n" if second_num != UPPER_LIMIT
    else f"{first_num: > 2} x {second_num: > 2} = {(first_num * second_num): > 2}\n\n"
    for seed_first_num in (LOW_LIMIT, LOW_LIMIT + COLUMNS)
    for second_num in range(LOW_LIMIT, UPPER_LIMIT + 1)
    for first_num in range(seed_first_num, seed_first_num + COLUMNS)
)
print(*table, end="\n")
def are_queens_safe(positions):
    """
    Проверяет, не бьют ли друг друга ферзи на доске 8x8.
    Аргументы:
    positions -- список кортежей, где каждый кортеж содержит
    координаты ферзя (строка, столбец)
    Возвращает:
    True, если ферзи не бьют друг друга; False в противном случае
    """
    attacked_rows = set()
    attacked_columns = set()
    attacked_diagonals = set()

    for pos in positions:
        row, column = pos
        if row in attacked_rows or column in attacked_columns or \
                ((column - row) in attacked_diagonals or (column + row) in attacked_diagonals):
            return False
        attacked_rows.add(row)
        attacked_columns.add(column)
        attacked_diagonals.add((column - row))
        attacked_diagonals.add((column + row))

    return True
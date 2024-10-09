class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self, points):
        if self.score + points > 1000:
            raise OverflowError("Очки не могут быть больше 1000.")
        self.score += points

    def subtract_score(self, points):
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points

# Пример использования класса GameScore:
game_score = GameScore()
try:
    game_score.add_score(500)
    print(f"Текущий счет: {game_score.score}")
    game_score.add_score(600)
except OverflowError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    game_score.subtract_score(600)
except ValueError as e:
    print(e)
finally:
    game_score.subtract_score(100)
    print(f"Текущий счет после вычитания: {game_score.score}")
import csv

class Student:
    def __init__(self, name, subjects_file):
        self._name = name
        self._subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == '_name' or name in ['add_grade', 'add_test_score']:
            super().__setattr__(name, value)
        else:
            first_letter = value[0].upper()
            valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if name[0] != first_letter or any(char not in valid_chars for char in name):
                raise ValueError(f"ФИО должно состоять только из букв и начинаться с заглавной буквы.")
            super().__setattr__(name, value)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if hasattr(self, '_subjects') and name in self._subjects:
                return self._subjects[name]
            raise AttributeError(f"Предмет '{name}' не найден")

    def __str__(self):
        return f"Студент: {self._name}\nПредметы: {list(self._subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                self._subjects[row[0]] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5.")
        self._subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, score):
        if not isinstance(score, int) or score < 0 or score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100.")
        self._subjects[subject]['test_scores'].append(score)

    def get_average_test_score(self, subject):
        scores = self._subjects[subject]['test_scores']
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        grades = [sum(self._subjects[subject]['grades']) / len(self._subjects[subject]['grades']) \
                  for subject in self._subjects if 'grades' in self._subjects[subject]]
        return sum(grades) / len(grades) if grades else 0


# Пример использования
if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
import os
import time


def remove_old_files(directory, days_threshold):
    """Удаляет файлы, которые не изменялись более заданного количества дней."""

    # Преобразуем дни в секунды
    threshold_seconds = days_threshold * 86400

    current_time = time.time()

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            last_modified_time = os.path.getmtime(file_path)

            if current_time - last_modified_time > threshold_seconds:
                print(f"Удаляю файл: {filename}")
                os.remove(file_path)


if __name__ == "__main__":
    directory = "/path/to/your/directory"
    days_threshold = 30  # Количество дней

    try:
        remove_old_files(directory, days_threshold)
    except Exception as e:
        print(f"Ошибка при удалении файлов: {e}")
import os


def find_files_by_extension(directory, extension):
    """Находит и перечисляет все файлы с заданным расширением в указанном каталоге и всех его подкаталогах."""

    matching_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.lower().endswith(extension):
                matching_files.append(file_path)

    return matching_files


if __name__ == "__main__":
    directory = "/path/to/your/directory"
    extension = ".txt"

    found_files = find_files_by_extension(directory, extension)
    if len(found_files) > 0:
        print("\nФайлы с расширением {}:".format(extension))
        for file in found_files:
            print(file)
    else:
        print("Не найдено файлов с расширением {}.".format(extension))
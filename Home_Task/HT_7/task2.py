import os
import zipfile


def create_archive(source_dir, destination_zip_path):
    """Создает архив ZIP из исходного каталога"""

    # Проверка наличия исходного каталога
    if not os.path.isdir(source_dir):
        raise ValueError(f"Каталог '{source_dir}' не найден")

    with zipfile.ZipFile(destination_zip_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)

                archive.write(file_path, arcname=relative_path)


if __name__ == "__main__":
    source_dir = "/path/to/source/directory/"
    destination_zip_path = "/path/to/destination/archive.zip"

    try:
        create_archive(source_dir, destination_zip_path)
        print(f"Архив успешно создан: {destination_zip_path}")
    except Exception as e:
        print(f"Ошибка при создании архива: {e}")
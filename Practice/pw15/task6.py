import os,sys
import pathlib
import collections
import logging
import argparse


PathInfo = collections.namedtuple('PathInfo', ['name', 'extension', 'is_dir', 'parent'])


def collect_directory_info(directory_path):
    directory_content = {}
    parent_directory = os.path.dirname(directory_path)

    for item in os.scandir(directory_path):
        relative_path = os.path.relpath(item.path, start=parent_directory)
        dir_name = os.path.basename(relative_path)
        extension = ''
        is_dir = False

        if item.is_file():
            _, ext = os.path.splitext(dir_name)
            extension = ext[1:]  # strip leading dot
            is_dir = False
        elif item.is_dir():
            extension = ''
            is_dir = True

        info = PathInfo(name=dir_name, extension=extension, is_dir=is_dir, parent=parent_directory)
        directory_content[relative_path] = info

    return directory_content


def save_data_to_file(directory_content, output_file):
    with open(output_file, 'w') as out_file:
        for path, data in directory_content.items():
            entry = ', '.join([f'{key}={value}' for key, value in data._asdict().items()])
            out_file.write(f'{entry}\n')


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory", help="Путь к директории для анализа")
    parser.add_argument("-o", "--output", default='directory_content.txt', help="Путь к выходному файлу")
    args = parser.parse_args()

    input_directory = pathlib.Path(args.input_directory)
    if not input_directory.exists():
        logging.error(f"Директория '{input_directory}' не существует.")
        return

    directory_content = collect_directory_info(input_directory)
    save_data_to_file(directory_content, args.output)


if __name__ == "__main__":
    main(sys.argv[1:])
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['ID', 'Name', 'Access_Level'])

        for access_level, users in data.items():
            for user_id, name in users.items():
                csv_writer.writerow([user_id, name, access_level])

json_to_csv('users.json', 'users.csv')


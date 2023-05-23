#!/usr/bin/python3
"""This module exports data gathered from an api in csv format"""

import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    response = requests.get(url)
    employee_name = response.json().get('username')

    task_response = requests.get(url + "/todos")
    tasks = task_response.json()

    csv_data = []
    for todo in tasks:
        csv_data.append([id, employee_name, todo.get('completed'),
                        todo.get('title')])

    with open('{}.csv'.format(id), 'w', newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)

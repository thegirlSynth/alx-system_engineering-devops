#!/usr/bin/python3
"""This module gathers data from an api"""

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    response = requests.get(url)
    employee_name = response.json().get('username')

    task_response = requests.get(url + "/todos")
    tasks = task_response.json()

    json_data = {str(id): []}
    for task in tasks:
        task_data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee_name
        }
        json_data[str(id)].append(task_data)

    with open('{}.json'.format(id), 'w') as file:
        json.dump(json_data, file)

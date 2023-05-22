#!/usr/bin/python3
"""This module records all tasks from all employees in JSON format"""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    users = response.json()

    all_data = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')

        tasks_url = url + '{}/todos'.format(id)
        task_response = requests.get(tasks_url)
        tasks = task_response.json()

        json_data = []
        for task in tasks:
            task_data = {
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed'),
            }
            json_data.append(task_data)
        all_data[str(id)] = json_data

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_data, file)

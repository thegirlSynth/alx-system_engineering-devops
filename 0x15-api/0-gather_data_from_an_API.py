#!/usr/bin/python3
"""This module gathers data from an api"""

import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    response = requests.get(url)
    employee_name = response.json().get('name')

    task_response = requests.get(url + "/todos")
    tasks = task_response.json()

    completed_tasks = [todo['title'] for todo in tasks if todo['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), len(tasks)))

    for task_title in completed_tasks:
        print("\t {}".format(task_title))

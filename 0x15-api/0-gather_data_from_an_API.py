#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id

    # Getting user name
    response = requests.get(url)
    name = response.json().get("name")

    # Getting todos
    response = requests.get(url + "/todos")
    todos = response.json()

    # Select completed tasks
    completed = [task for task in todos if task['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task.get('title')))

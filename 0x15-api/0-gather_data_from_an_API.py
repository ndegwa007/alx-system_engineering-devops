#!/usr/bin/python3
"""a script that shows employees progress completing tasks
    from all the allocated tasks"""
import requests
import sys


def get_employee_progress(employee_id):
    """ get the api url and find employee progress """

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # retrieve employee info
    resp = requests.get(employee_url)
    resp.raise_for_status()
    employee_data = resp.json()

    # retrieve employee todo list
    resp = requests.get(todos_url)
    resp.raise_for_status()
    todos_data = resp.json()

    # extract relevant info
    employee_name = employee_data['name']
    todo_task = len(todos_data)
    completed_tasks = [
            todo['title'] for todo in todos_data if todo['completed']]

    # display progress info
    print(f"Employee {employee_name} is done with \
tasks({len(completed_tasks)}/{todo_task}):")

    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    """ get the employee progress """
    employee_id = sys.argv[1]
    get_employee_progress(employee_id)

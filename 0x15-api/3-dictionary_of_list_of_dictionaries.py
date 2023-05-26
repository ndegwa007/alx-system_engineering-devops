#!/usr/bin/python3
"""script creates a json file that shows all tasks for all employees"""
import json
import requests
import sys


def export_todo_all_employees_json():
    base_url = "https://jsonplaceholder.typicode.com"
    employees_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        # Retrieve employees information
        response = requests.get(employees_url)
        response.raise_for_status()
        employees_data = response.json()

        # Retrieve TODO list for all employees
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Prepare JSON file name
        file_name = "todo_all_employees.json"

        # Prepare data for JSON export
        json_data = {}
        for employee in employees_data:
            user_id = employee['id']
            username = employee['username']
            json_data[user_id] = []
            for todo in todos_data:
                if todo['userId'] == user_id:
                    task_completed_status = todo['completed']
                    task_title = todo['title']
                    json_data[user_id].append(
                            {"username": username,
                                "task": task_title,
                                "completed": task_completed_status})

        # Export data to JSON file
        with open(file_name, 'w') as jsonfile:
            json.dump(json_data, jsonfile)

        # print(f"JSON file '{file_name}' exported successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        return


if __name__ == '__main__':
    export_todo_all_employees_json()

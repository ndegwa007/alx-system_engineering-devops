#!/usr/bin/python3
"""script creates a json file with all necessary
task info for employee"""

import json
import requests
import sys


def export_employee_todo_json(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Retrieve employee information
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Retrieve employee's TODO list
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Extract relevant information
        username = employee_data['username']

        # Prepare JSON file name
        file_name = f"{employee_id}.json"

        # Prepare data for JSON export
        json_data = {employee_id: []}
        for todo in todos_data:
            task_completed_status = todo['completed']
            task_title = todo['title']
            json_data[employee_id].append(
                    {"task": task_title,
                        "completed": task_completed_status,
                        "username": username})

        # Export data to JSON file
        with open(file_name, 'w') as jsonfile:
            json.dump(json_data, jsonfile)

        print(f"JSON file '{file_name}' exported successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        return


if __name__ == '__main__':
    employee_id = sys.argv[1]
    export_employee_todo_json(employee_id)

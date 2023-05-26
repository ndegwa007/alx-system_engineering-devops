#!/usr/bin/python3
"""a script that shows employees all the allocated tasks and writes it to a csv file"""
import requests
import sys
import csv

def get_employee_progress_to_csv(employee_id):
    """ get the api url and find employee progress """

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # retrieve employee info
    resp = requests.get(employee_url)
    resp.raise_for_status()
    employee_data = resp.json()
    print(employee_data)
    return
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

    """csvheader = ["userId", "username", "completed","title"]
    output = []

    for i in employee_data:
        listing = [i['userId'], i['username'], i['completed'], i['title']]
        output.append(listing]

    with open(f"{employers_id}.csv", "w", "utf-8", newline="") as f:
        writer = csv.writer(f)
        
        csv.writerow(csvheader)
        csv.writerows(output)"""


#if __name__ == '__main__':
    """ write the employee progress to a csv file """
    

#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://example.com/api"  # Replace with the actual API endpoint
    employee_url = f"{base_url}/employees/{employee_id}"
    todo_url = f"{base_url}/employees/{employee_id}/todo"

    # Fetch employee information
    response_employee = requests.get(employee_url)
    response_todo = requests.get(todo_url)

    if response_employee.status_code != 200 or response_todo.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    employee_data = response_employee.json()
    todo_data = response_todo.json()

    employee_name = employee_data.get("name")
    done_tasks = sum(task.get("completed") for task in todo_data)
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")

    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

#!/usr/bin/python3
"""For a given employee ID, returns information about his/her
   TODO list progress."""

import requests
from sys import argv

def fetch_user_info(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    return response.json()

def fetch_todo_list(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    return response.json()

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
        exit(1)
    
    user_id = argv[1]
    
    try:
        user_info = fetch_user_info(user_id)
        todo_list = fetch_todo_list(user_id)
        
        completed_tasks = [task for task in todo_list if task['completed']]
        
        print("Employee {} is done with tasks ({}/{}):".format(user_info['name'], len(completed_tasks), len(todo_list)))
        for task in completed_tasks:
            print("\t{}".format(task['title']))
            
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        exit(1)

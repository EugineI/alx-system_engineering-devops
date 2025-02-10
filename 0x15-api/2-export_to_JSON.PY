#!/usr/bin/python3
"""
fetches done tasks from todo-lists
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("username")

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    todos = todos_response.json()
    tasks_list = []
    for task in todos:
        tasks_list.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
                })
    json_data = {employee_id: tasks_list}
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file)

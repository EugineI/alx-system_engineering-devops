#!/usr/bin/python3
"""
fetches done tasks from todo-lists
"""
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
    employee_name = user_data.get("name")

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    todos = todos_response.json()
    TT = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done_task = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks ({done_task}/{TT}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

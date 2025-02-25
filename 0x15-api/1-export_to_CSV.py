#!/usr/bin/python3
"""
fetches done tasks from todo-lists
"""
import csv
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

    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([employee_id,
                             employee_name,
                             task.get("completed"),
                             task.get("title")])

#!/usr/bin/python3
"""
fetches done tasks from todo-lists
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    tasks_by_user = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        tasks_by_user[user_id] = []
        for task in todos:
            if task["userId"] == user_id:
                tasks_by_user[user_id].append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file)

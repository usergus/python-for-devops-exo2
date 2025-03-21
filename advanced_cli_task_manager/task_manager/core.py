import json
import os
from task_manager.logger import setup_logger

TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")
logger = setup_logger()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {task}")
    print(f"✅ Task added with ID {task_id}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} (Priority: {task['priority']})")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"❌ Task ID {task_id} not found.")
        return
    save_tasks(updated_tasks)
    logger.info(f"Deleted task with ID {task_id}")
    print(f"🗑️ Task ID {task_id} deleted.")

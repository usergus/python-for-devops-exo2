import unittest
import os
import json
from task_manager.core import add_task, delete_task, load_tasks, save_tasks

TEST_FILE = "test_tasks.json"

# Patch the TASKS_FILE env var
os.environ["TASKS_FILE_PATH"] = TEST_FILE

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        save_tasks([])  # Reset file before each test

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        add_task("Test Task", 2)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test Task")
        self.assertEqual(tasks[0]["priority"], 2)

    def test_delete_task(self):
        add_task("Task to Delete", 1)
        tasks = load_tasks()
        task_id = tasks[0]["id"]
        delete_task(task_id)
        updated_tasks = load_tasks()
        self.assertEqual(len(updated_tasks), 0)

if __name__ == "__main__":
    unittest.main()

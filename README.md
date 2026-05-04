# Task Manager CLI

A command-line task manager built with Python that lets you add, view, delete, and track tasks directly from the terminal. Tasks are saved to a JSON file so your data persists even after you close the program.

## What It Does

You get an interactive menu in the terminal. You can add tasks with a priority level, view all your tasks with their status, mark them as done, delete individual tasks, or clear all completed tasks at once. Everything is stored locally in a `tasks.json` file.

## How It Works (Step by Step)

1. When the program starts, it calls `load_tasks()` which checks if `tasks.json` already exists using `os.path.exists`.
2. If the file exists, it opens it in read mode and loads the data using `json.load`. If the file is corrupted or unreadable, it catches the `json.JSONDecodeError` and starts fresh with an empty list.
3. If the file does not exist yet, it returns an empty list and the file gets created on the first save.
4. The program then enters a `while True` loop showing a menu with 6 options. You pick a number and the matching function runs.

**Adding a task** — you type the task name, then choose a priority from High, Medium, or Low. The input is validated in a loop until you enter a valid option. The task is then appended to the list as a dictionary with the task name, done status, priority, and a timestamp using `datetime.now().isoformat()`. Then `save_tasks()` is called which opens the file in write mode and dumps the updated list using `json.dump`.

**Viewing tasks** — loops through the task list using `enumerate` and prints each task with its number, a checkmark or cross for status, priority, and the timestamp it was added.

**Deleting a task** — shows the task list first, asks for a number, validates the range, then removes it using `list.pop(task - 1)`. The minus one accounts for the list being zero-indexed while the display starts from one.

**Marking as done** — same flow as delete but instead of removing the task it sets `task["Done"] = True` and saves.

**Clearing done tasks** — uses a list comprehension to filter out all tasks where `Done` is True, replaces the task list with the filtered version, and saves.

## Project Structure

```
Task_manager_Cli/
├── task_manager.py
└── tasks.json          (auto-created on first run)
```

## Requirements

- Python 3.x
- No external libraries needed. Only `os`, `json`, and `datetime` from Python's standard library.

## How to Run

```
python task_manager.py
```

**Example session:**

```
 --Main menu--
    1. Add a task
    2. View tasks
    3. Delete Tasks
    4. Mark Tasks as done
    5. Clear done tasks
    6. Exit

Enter your choice: 1
Enter the task you want to add: Submit assignment
Enter the priority of the task (High, Medium, Low): High
Task added successfully!

Enter your choice: 2
1.[ ❌ ] Submit assignment , High Priority , Added on: 2025-04-01T22:14:03
```

## Built With

- `os` — for checking if the tasks file exists
- `json` — for reading and writing task data persistently
- `datetime` — for timestamping each task at the time it is added

## Author

Muhammad Saqib — BS Software Engineering, Air University Islamabad  
GitHub: [Muhammad-Saqib-eng](https://github.com/Muhammad-Saqib-eng)

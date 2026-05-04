import json
import os
from datetime import datetime

FILE_NAME="tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to decode tasks. Starting with an empty task list.")
            return []
    return []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file,indent=4)  

tasks=load_tasks()

def add_tasks():
     task=input("Enter the task you want to add: ")
     while True:
        input_priority=input("Enter the priority of the task (High, Medium, Low): ").capitalize()
        if input_priority in ["High","Medium","Low"]:
            break
        else:
            print("Invalid priority. Please enter High, Medium, or Low.")

     tasks.append({"task": task, "Done": False, "Priority": input_priority, "Timestamp": datetime.now().isoformat()})
     save_tasks()
     print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return 
    else:
      for i,task in enumerate(tasks,start=1):
        status= " ✔️ " if task["Done"] else " ❌ "
        print(f"{i}.[{status}] {task['task']} , {task.get('Priority','Not specified')} Priority , Added on: {task.get('Timestamp','Unknown')}")
        
def check_tasks():
    if not tasks:
        print("No tasks found!")
        return False
    return True

def delete_tasks():
    if not check_tasks():
        return
    view_tasks()
    try:
        task=int(input("Enter the task number you want to delete: "))
        if 1<=task<=len(tasks): 
            tasks.pop(task-1)
            print("Task deleted successfully!")
            save_tasks()
        else:
            print("Task not found!")

    except ValueError:
        print("Invalid input. Please enter a number.")


def mark_tasks_done():
    if  not check_tasks():
        return
    
    view_tasks()
    try:
        task=int(input("Enter the task number you want to mark as done: "))
        if 1<=task<=len(tasks): 
            tasks[task-1]["Done"]=True
            save_tasks()
            print("Task marked as done!")
        else:
            print("Task not found!")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def clear_done_tasks():
    global tasks
    done_tasks=[task for task in tasks if task["Done"]]
    if not done_tasks:
        print("No done tasks to clear!")
        return
    else:
        tasks=[task for task in tasks if not task["Done"]]
        save_tasks()    
        print("Done tasks cleared successfully!")

while True:

    menu= """ --Main menu--
    1. Add a task
    2. View tasks
    3. Delete Tasks
    4.Mark Tasks as done
    5.Clear done tasks
    6. Exit
    """

    print(menu)
    try:
        choice= int(input("Enter your choice: "))

        if choice==1:
            add_tasks()

        elif choice==2:
            view_tasks()    


        elif choice==3:
            
            delete_tasks()

        elif choice==4:
            
            mark_tasks_done()

        elif choice==5:
            input_clear=input("Are you sure you want to clear all done tasks? (yes/no): ").lower()
            if input_clear=="yes":
                clear_done_tasks()
            else:
                print("Clear done tasks cancelled.")

        elif choice==6:
           
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    


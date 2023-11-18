import sys
import os

def add_task(task):
  tasks.append(task)

def list_tasks():
  for task in tasks:
    print("  -",task)

def mark_task_done(task):
  tasks.remove(task)


tasks = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task\n2. List tasks\n3. Mark a task as done\n4. Exit")
    print("Enter your choice : ",end="")

    choice = input()

    if choice == "1":
      task = input("Enter a task: ")
      add_task(task)
    elif choice == "2":
      list_tasks()
    elif choice == "3":
      task = input("Enter a task to mark as done: ")
      mark_task_done(task)
    elif choice == "4":
      sys.exit()
    else:
      print("Invalid choice.")

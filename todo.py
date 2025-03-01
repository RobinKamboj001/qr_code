import os

tasks = []

def add_task():
    task = input("Ener Your Task = ")
    if task in tasks:
        print(f"Your Task {task} Alredy Axist")
    else:
        tasks.append(task)
        print(f"Your Task {task} Succsessfuly Added")

def viwe_task():
    if tasks:
        print("All Task")
        for i,task in enumerate(tasks, 1):
            print(f"{i}, {task}")
    else:
        print("Not Found Task")

def delet_task():
    task = input("Enter Task Name You Have Deleted = ")
    if task in tasks:
        tasks.remove(task)
    else:
        print(f"Task {task} Not Nound")

def clear_task():
    tasks.clear()
    print("All Task Clear Successfuly")

while True:
    try:
        print("Task Manegment App")
        print("1. Add Task")
        print("2. Viwe Task")
        print("3. Delet Task")
        print("4. Clear Task")
        print("5. Exit Task Manegment App")

        select = int(input("Enter Your Number(1/5) = "))

        if select == 1:
            add_task()
        elif select == 2:
            viwe_task()
        elif select == 3:
            delet_task()
        elif select == 4:
            clear_task()
        elif select == 5:
            print("Exit App")
        else:
            print("Plese Selact Right Number")
    except ValueError:
        print("Rong Number Selacted")

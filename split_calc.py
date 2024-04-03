import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, due_date, category, completed=False):
        self.name = name
        self.due_date = due_date
        self.category = category
        self.completed = completed

def validate_total_amount():
    try:
        total_amount = float(total_amount_entry.get())
        if total_amount <= 0:
            raise ValueError("Total amount must be a positive number.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False
    return True

def validate_num_people():
    try:
        num_people = int(num_people_entry.get())
        if num_people <= 0:
            raise ValueError("Number of people must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False
    return True

def validate_task_name():
    task_name = task_name_entry.get().strip()
    if not task_name:
        messagebox.showerror("Error", "Task name cannot be empty.")
        return False
    return True

def validate_due_date():
    due_date = due_date_entry.get().strip()
    if not due_date:
        messagebox.showerror("Error", "Due date cannot be empty.")
        return False
    # You can add more sophisticated date validation logic here if needed
    return True

def validate_category():
    category = category_entry.get().strip()
    if not category:
        messagebox.showerror("Error", "Category cannot be empty.")
        return False
    return True

def calculate_split():
    if not (validate_total_amount() and validate_num_people()):
        return
    total_amount = float(total_amount_entry.get())
    num_people = int(num_people_entry.get())
    individual_share = total_amount / num_people
    messagebox.showinfo('Split Calculation', f'Each person should pay ${individual_share:.2f}')

def add_task():
    if not (validate_task_name() and validate_due_date() and validate_category()):
        return
    name = task_name_entry.get()
    due_date = due_date_entry.get()
    category = category_entry.get()

    task = Task(name, due_date, category)
    tasks.append(task)
    save_tasks_to_file()
    update_task_list()
    messagebox.showinfo('Success', 'Task added successfully!')

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, f"{task.name} - Due: {task.due_date}, Category: {task.category}")

def save_tasks_to_file():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task.name},{task.due_date},{task.category}\n")

def load_tasks_from_file():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                task = Task(data[0], data[1], data[2])
                tasks.append(task)
    except FileNotFoundError:
        pass

tasks = []

root = tk.Tk()
root.title('Task Scheduler')

# GUI elements for total amount splitting

tk.Label(root, text='Total Amount ($):').grid(row=0, column=0, padx=10, pady=5)
total_amount_entry = tk.Entry(root)
total_amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text='Number of People:').grid(row=1, column=0, padx=10, pady=5)
num_people_entry = tk.Entry(root)
num_people_entry.grid(row=1, column=1, padx=10, pady=5)

split_button = tk.Button(root, text='Calculate Split', command=calculate_split)
split_button.grid(row=2, column=0, columnspan=2, pady=10)

# GUI elements for task scheduling

tk.Label(root, text='Task Name:').grid(row=3, column=0, padx=10, pady=5)
task_name_entry = tk.Entry(root)
task_name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text='Due Date:').grid(row=4, column=0, padx=10, pady=5)
due_date_entry = tk.Entry(root)
due_date_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text='Category:').grid(row=5, column=0, padx=10, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=5, column=1, padx=10, pady=5)

add_button = tk.Button(root, text='Add Task', command=add_task)
add_button.grid(row=6, column=0, columnspan=2, pady=10)

task_list = tk.Listbox(root, width=50, height=10)
task_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

load_tasks_from_file()
update_task_list()

root.mainloop()

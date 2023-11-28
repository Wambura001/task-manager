import sqlite3
from tkinter import *

# Function to initialize the database and create the tasks table
def initialize_database():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task_text TEXT
                     )''')
    conn.commit()
    conn.close()

# Function to delete all finished tasks based on checked checkbuttons
def delete_finished_tasks():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task_text FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        task_id, task_text = task
        if task_var[task_id].get() == 1:
            cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()

# Function to display tasks with a check button next to each task
def show_tasks_with_checkbuttons():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task_text FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    for task in tasks:
        task_id, task_text = task
        task_var[task_id] = IntVar()
        check_button = Checkbutton(window, text=task_text, variable=task_var[task_id])
        check_button.pack()

# Initialize the database
initialize_database()

# Create Tkinter GUI
window = Tk()
window.title('Task Manager')
window.geometry('500x500')

# Dictionary to store IntVar for each task
task_var = {}

# Display tasks with a check button next to each task
show_tasks_with_checkbuttons()

# Button to trigger the deletion of finished tasks
delete_finished_button = Button(window, text="Delete Finished Tasks", command=delete_finished_tasks)
delete_finished_button.pack()

# Run the Tkinter GUI
window.mainloop()

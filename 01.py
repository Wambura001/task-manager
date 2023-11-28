from tkinter import *
import sqlite3

#create database
def initialize_database():
  conn = sqlite3.connect("task_manager.db")
  cursor = conn.cursor()
  
  #Create table to store tasks
  cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      task_text TEXT
                    )''')
  
  #close connection
  conn.commit()
  conn.close()
  
#submit 
def submit():
  task = input_var.get()

  #open database connection
  conn = sqlite3.connect('task_manager.db')
  cursor = conn.cursor()

  #insert task into the database
  cursor.execute('INSERT INTO tasks (task_text) VALUES (?)', (task,))

  #close connection
  conn.commit()
  conn.close()

  #clear the input field
  input_var.set('')

  #Display added task
  show_tasks()
    
#retrieve tasks from database and update task_label
def show_tasks():
  #open database connection
  conn = sqlite3.connect('task_manager.db')
  cursor = conn.cursor()

  #fetch all tasks from database
  cursor.execute('SELECT task_text FROM tasks')
  tasks = cursor.fetchall()

  #close connection
  conn.close()

  #Display all tasks
  task_label['text'] = '\n'.join(str(task[0]) for task in tasks)

#initialize database
initialize_database()

#GUI
window = Tk()
window.title('task_manager')
window.geometry('500x500')

#create texts and inputs
add_label = Label(window, text =('Please add text below to add to your task manager'))
input_var = StringVar()
input_entry = Entry(window, textvariable=input_var)
submit_button = Button(window, text='Add', command=submit)
task_label = Label(window, text = '')

#place texts and inputs
add_label.pack(side=TOP)
input_entry.pack()
submit_button.pack()
task_label.pack()

window.mainloop()







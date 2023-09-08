import tkinter as tk

root = tk.Tk()
root.title("ToDo list")

tasks = []

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

def add_task():
    new_task = task_entry.get()
    if new_task:
        tasks.append(new_task)
        task_listbox.insert(tk.END, new_task)
        task_entry.delete(0, tk.END)
        pass

add_button = tk.Button(root, text="Enter task", command=add_task)
add_button.pack()  

task_listbox = tk.Listbox(root, width=60)
task_listbox.pack(pady=10)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_task_index = selected_task[0]
        del tasks[selected_task_index]
        task_listbox.delete(selected_task_index)
        pass

for task in tasks:
    task_listbox.insert(tk.END, task)

delete_button = tk.Button(root, text="Delete task", command=delete_task)
delete_button.pack()

root.mainloop()
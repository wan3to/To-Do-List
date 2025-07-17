import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Зареждане на задачи от файл
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Запазване на задачи във файл
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Добавяне на нова задача
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Грешка", "Въведи задача!")

# Изтриване на избрана задача
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Грешка", "Няма избрана задача!")

# --- Графичен интерфейс ---
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")
root.config(bg="#f0f0f0")

tasks = load_tasks()

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

# Зареждане на съществуващи задачи
for task in tasks:
    listbox.insert(tk.END, task)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Добави задача", command=add_task, bg="#4CAF50", fg="white")
add_btn.pack(pady=2)

delete_btn = tk.Button(root, text="Изтрий задача", command=delete_task, bg="#f44336", fg="white")
delete_btn.pack(pady=2)

root.mainloop()
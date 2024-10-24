import tkinter as tk
from tkinter import messagebox
import json


class TaskManager:
    def __init__(self, data_file='tasks.json'):
        self.data_file = data_file
        self.task_list = []
        self.load_data()

   
    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.task_list = json.load(file)
                # Ensure all tasks have 'details' and 'done' fields
                for task in self.task_list:
                    if 'details' not in task:
                        task['details'] = "Unnamed Task"
                    if 'done' not in task:
                        task['done'] = False
        except FileNotFoundError:
            self.task_list = []

    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.task_list, file, indent=4)

    
    def create_task(self, details):
        new_task = {'details': details, 'done': False}
        self.task_list.append(new_task)
        self.save_data()

    
    def remove_task(self, idx):
        if 0 <= idx < len(self.task_list):
            del self.task_list[idx]
            self.save_data()

    
    def modify_task(self, idx, updated_details):
        if 0 <= idx < len(self.task_list):
            self.task_list[idx]['details'] = updated_details
            self.save_data()

    
    def mark_as_done(self, idx):
        if 0 <= idx < len(self.task_list):
            self.task_list[idx]['done'] = True
            self.save_data()

# GUI class to handle the Tkinter-based interface
class TaskApp:
    def __init__(self, window):
        self.manager = TaskManager()
        self.window = window
        self.window.title("Task Management App")

        
        self.input_frame = tk.Frame(window)
        self.input_frame.pack(padx=10, pady=10)

        
        self.input_field = tk.Entry(self.input_frame, width=40)
        self.input_field.pack(side=tk.LEFT, padx=5)

        
        self.add_btn = tk.Button(self.input_frame, text="Add Task", command=self.add_new_task)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        
        self.list_frame = tk.Frame(window)
        self.list_frame.pack(padx=10, pady=10)

        
        self.task_listbox = tk.Listbox(self.list_frame, height=10, width=40)
        self.task_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.update_task_display()

        
        self.button_frame = tk.Frame(self.list_frame)
        self.button_frame.grid(row=0, column=1, padx=10, pady=10)

        
        self.done_btn = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done)
        self.done_btn.pack(fill=tk.X, pady=5)

        
        self.update_btn = tk.Button(self.button_frame, text="Update Task", command=self.modify_selected_task)
        self.update_btn.pack(fill=tk.X, pady=5)

        
        self.delete_btn = tk.Button(self.button_frame, text="Delete Task", command=self.remove_selected_task)
        self.delete_btn.pack(fill=tk.X, pady=5)

    
    def add_new_task(self):
        task_details = self.input_field.get()
        if task_details:
            self.manager.create_task(task_details)
            self.input_field.delete(0, tk.END)
            self.update_task_display()
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    
    def mark_done(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            self.manager.mark_as_done(selected_idx)
            self.update_task_display()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

   
    def modify_selected_task(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            updated_task = self.input_field.get()
            if updated_task:
                self.manager.modify_task(selected_idx, updated_task)
                self.input_field.delete(0, tk.END)
                self.update_task_display()
            else:
                messagebox.showwarning("Input Error", "Please enter new task details.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    
    def remove_selected_task(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            self.manager.remove_task(selected_idx)
            self.update_task_display()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    
    def update_task_display(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.task_list:
            
            details = task.get('details', "Unnamed Task")
            status = "✔️" if task.get('done', False) else "❌"
            self.task_listbox.insert(tk.END, f"{details} [{status}]")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

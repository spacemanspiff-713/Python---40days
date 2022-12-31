import tkinter as tk

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.todos = []

        self.title("Todo App")

        # Create the main frame
        main_frame = tk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)

        # Create the todo list frame
        todo_list_frame = tk.Frame(main_frame)
        todo_list_frame.pack(side="left", fill="both", expand=True)

        # Create the todo list scrollbar
        todo_list_scrollbar = tk.Scrollbar(todo_list_frame)
        todo_list_scrollbar.pack(side="right", fill="y")

        # Create the todo list
        self.todo_list = tk.Listbox(todo_list_frame, yscrollcommand=todo_list_scrollbar.set)
        self.todo_list.pack(side="left", fill="both", expand=True)
        todo_list_scrollbar.config(command=self.todo_list.yview)

        # Create the todo controls frame
        todo_controls_frame = tk.Frame(main_frame)
        todo_controls_frame.pack(side="right", fill="both")

        # Create the add todo button
        add_button = tk.Button(todo_controls_frame, text="Add", command=self.add_todo)
        add_button.pack(side="top", fill="x")

        # Create the edit todo button
        edit_button = tk.Button(todo_controls_frame, text="Edit", command=self.edit_todo)
        edit_button.pack(side="top", fill="x")

        # Create the delete todo button
        delete_button = tk.Button(todo_controls_frame, text="Delete", command=self.delete_todo)
        delete_button.pack(side="top", fill="x")

        # Create the mark complete todo button
        mark_complete_button = tk.Button(todo_controls_frame, text="Mark Complete", command=self.mark_complete)
        mark_complete_button.pack(side="top", fill="x")

    def add_todo(self):
        # Add a new todo to the list
        todo_text = self.ask_for_todo_text()
        if todo_text:
            self.todos.append(todo_text)
            self.update_todo_list()

    def edit_todo(self):
        # Edit the selected todo
        selected_index = self.todo_list.curselection()
        if not selected_index:
            return
        selected_index = selected_index[0]
        todo_text = self.ask_for_todo_text()
        if todo_text:
            self.todos[selected_index] = todo_text

    def delete_todo(self):
        # Delete the selected todo
        selected_index = self.todo_list.curselection()
        if not selected_index:
            return
        selected_index = selected_index[0]
        del self.todos[selected_index]
        self.update_todo_list()

    def mark_complete(self):
        # Mark the selected todo as complete
        selected_index = self.todo_list.curselection()
        if not selected_index:
            return
        selected_index = selected_index[0]
        self.todos[selected_index] = f"✓ {self.todos[selected_index]}"
        self.update_todo_list()

    def update_todo_list(self):
        # Update the todo list with the current todos
        self.todo_list.delete(0, "end")
        for todo in self.todos:
            self.todo_list.insert("end", todo)

    def ask_for_todo_text(self):
        # Show a dialog to get the text for a new or edited todo
        todo_text = None
        def save_todo_text():
            nonlocal todo_text
            todo_text = todo_text_entry.get()
            dialog.destroy()

        dialog = tk.Toplevel(self)
        dialog.title("Enter Todo Text")
        dialog.geometry("200x100")

        todo_text_label = tk.Label(dialog, text="Todo Text:")
        todo_text_label.pack(side="top", fill="x")

        todo_text_entry = tk.Entry(dialog)
        todo_text_entry.pack(side="top", fill="x")

        save_button = tk.Button(dialog, text="Save", command=save_todo_text)
        save_button.pack(side="bottom", fill="x")

        dialog.wait_window()

        return todo_text

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
import functions
import PySimpleGUI as sg

# ADD FIELDS
add_label = sg.Text('Type In A Todo')
add_input_box = sg.InputText(tooltip='Enter Todo', key="todo")
add_button = sg.Button("Add")

show_todos = sg.Listbox(values=functions.get_todos('todo_app/todo.txt'), size=(60,15))


app_window = sg.Window('Todo App', 
                        layout=[[add_label], 
                        [add_input_box, add_button],
                        [show_todos]], 
                        font=('Helvetica', 20))


while True:
    event, values = app_window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            functions.add_todo(values["todo"])
        case sg.WIN_CLOSED:
            break
app_window.close()
import functions
import PySimpleGUI as sg

# ADD FIELDS
add_label = sg.Text('Type In A Todo')
add_input_box = sg.InputText(tooltip='Enter Todo', key="todo")
add_button = sg.Button("Add")

show_todos = sg.Listbox(values=functions.get_todos('todo_app/todo.txt'), 
                        size=(60,15), key="todo_list", enable_events=True)
edit_button = sg.Button("Edit")


app_window = sg.Window('Todo App', 
                        layout=[[add_label], 
                        [add_input_box, add_button],
                        [show_todos, edit_button]], 
                        font=('Helvetica', 20))


while True:
    event, values = app_window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            functions.add_todo(values["todo"])
            todo_list = functions.get_todos('todo_app/todo.txt')
            app_window['todo_list'].update(values=todo_list)

        case "Edit":
            todo_to_edit = values['todo_list'][0]
            new_todo = values['todo']
            todo_list = functions.get_todos('todo_app/todo.txt')
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.edit_todos(todo_list)
            app_window['todo_list'].update(values=todo_list)

        case 'todo_list':
            app_window['todo'].update(value=values['todo_list'])
        case sg.WIN_CLOSED:
            break
app_window.close()
import functions
import PySimpleGUI as sg

# ADD FIELDS
add_label = sg.Text('Type In A Todo')
add_input_box = sg.InputText(tooltip='Enter Todo', key="todo")
add_button = sg.Button("Add")


app_window = sg.Window('Todo App', 
                        layout=[[add_label], 
                        [add_input_box, add_button]], 
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
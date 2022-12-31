import functions
import PySimpleGUI as sg

label = sg.Text('Type In A Todo')
input_box = sg.InputText(tooltip='Enter Todo')
add_button = sg.Button("Add")

app_window = sg.Window('Todo App', layout=[[label], [input_box, add_button]])
app_window.read()
app_window.close()
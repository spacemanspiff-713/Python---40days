import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destiniation folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compression_button = sg.Button("Compress")

window = sg.Window("File Compessor", 
                    layout=[[label1,input1,choose_button1],
                            [label2,input2,choose_button2],
                            [compression_button]])
window.read()
window.close()
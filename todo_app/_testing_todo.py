from functions import *
import time



todo_list = open("todo_app/todo.txt", "r")

while True:
    prompt_todo = input("Type add, show, edit, complete, or quit: ")
    prompt_todo = prompt_todo.strip()
    if prompt_todo.startswith('add'):
        current_time = time.strftime("%b %d, %Y at %H:%M:%S")
        add_todo = f"{prompt_todo[4:]} {current_time} \n"
        file = open("todo_app/todo.txt", "a")
        file.writelines(add_todo)
        file.close()
    elif prompt_todo.startswith('show'):
        print_list('todo_app/todo.txt')
    elif prompt_todo.startswith('edit'):
        print_list('todo_app/todo.txt')
        file = open('todo_app/todo.txt', 'r')
        todo_list = file.readlines()
        file.close()
        try:
            edit_list = int(input("Select which number you wish to edit: "))
            new_todo = input("Edit the todo: ")
            todo_list[edit_list - 1] = new_todo
            file = open('todo_app/todo.txt', 'w')
            file.writelines(todo_list)
            file.close()
        except ValueError:
            print("Your response is not valid, please try again.")
            prompt_todo = input("Type add, show, edit, complete, or quit: ")
            prompt_todo = prompt_todo.strip()
    elif prompt_todo.startswith('complete'):
        print_list('todo_app/todo.txt')
        file = open('todo_app/todo.txt', 'r')
        todo_list = file.readlines()
        file.close()
        try:
            edit_list = int(input("Select which number you wish to complete: "))
            todo_list.pop(edit_list - 1)
            file = open('todo_app/todo.txt', 'w')
            file.writelines(todo_list)
            file.close()
        except IndexError:
            print("There is no todo there")
    elif prompt_todo.startswith('quit'):
        break
    else:
        print("I did not understand, please try again")
    
    

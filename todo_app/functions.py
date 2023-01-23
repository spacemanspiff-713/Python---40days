import time
FILEPATH = 'todo.txt'


def print_list(filepath):
    with open(filepath,'r') as file:
        todo_list = file.readlines()
    for index, x in enumerate(todo_list):
                print(f"{index + 1}:", x.strip("\n"))

def get_todos(filepath):
    with open(filepath,'r') as file:
        todo_list = file.readlines()
    return todo_list


def add_todo(input):
    # current_time = time.strftime("%b %d, %Y")
    add_todo = f"{input} \n"
    file = open("todo.txt", "a")
    file.writelines(add_todo)
    file.close()

def edit_todos(todos, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)
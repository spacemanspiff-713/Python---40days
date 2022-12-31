def print_list(filepath):
    with open(filepath,'r') as file:
        todo_list = file.readlines()
    for index, x in enumerate(todo_list):
                print(f"{index + 1}:", x.strip("\n"))

def get_todos(filepath):
    with open(filepath,'r') as file:
        todo_list = file.readlines()
    return todo_list
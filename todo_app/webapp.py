import streamlit as st
import functions

FILEPATH = 'todo.txt'
todos = functions.get_todos('todo.txt')

def add_todo():
    todo = st.session_state["new_todo"]
    functions.add_todo(todo)

st.title("My Todo App")
st.subheader("An app for listing todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.edit_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Add todo here", on_change=add_todo, key='new_todo')
st.session_state
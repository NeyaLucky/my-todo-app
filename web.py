import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # очищає поле після додавання

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    todo_clean = todo.strip()  # без \n
    checkbox = st.checkbox(todo_clean, key=todo_clean)  # унікальний ключ
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_clean]
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

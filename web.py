import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.writetodos(todos)


todos = functions.gettodos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writetodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a todo...",
              on_change=add_todo, key='new_todo')

print('hello')
FILEPATH = 'todos.txt'

def gettodos(filename = FILEPATH):
    with open(FILEPATH, 'r') as file:
        content = file.readlines()
    return content


def writetodos(todos ,filename = FILEPATH):
    with open(FILEPATH, 'w') as file:
        file.writelines(todos)
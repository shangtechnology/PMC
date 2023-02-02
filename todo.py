# Sample
user_prompt = 'Type add, show, edit or exit: '
todos = []
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input ('Enter a todo: ')
        todos.append(todo)
    elif user_action == 'show':
        for item in todos:
            print(item)
    elif user_action == 'edit':
        number = int(input ("number of item to edit"))
        number = number -1
        new_todo = input('Ener new todo: ')
        todos[number] = new_todo
    else:
        break

print ('Bye')

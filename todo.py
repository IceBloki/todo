while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for num, item in enumerate(todos):
                print("{}. {}".format(num + 1, item.capitalize().strip('\n')))

        case 'edit':
            number = int(input("What number of todo you want to edit? "))
            number -= 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo list to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break

print('Ciao')


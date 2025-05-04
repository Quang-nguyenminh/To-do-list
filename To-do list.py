todo_list = [['No.', 'Deadline', 'Task', 'Check']]


def mark():
    if len(todo_list) == 1:
        print('You have no task to mark.')
        input('\nPress Enter to continue.')
    else:
        for item in todo_list:
            print("{:<3}| {:<10}| {:<20}| {:<5}".format(item[0], item[1], item[2], item[3]))
        a = int(input('Mark task number: '))
        if 0 < a < len(todo_list):
            b = todo_list[a]
            b[3] = 'O'
            todo_list[a] = b
        else:
            print('\nError. Please try again.')


def incomplete():
    pass


def complete():
    pass


def view():
    if len(todo_list) == 1:
        print('You have no task on your to-do list.')
    else:
        for item in todo_list:
            print("{:<3}| {:<10}| {:<20}| {:<5}".format(item[0], item[1], item[2], item[3]))
    input('\nPress Enter to continue.')


def add():
    no = len(todo_list)
    deadline = input('Input deadline: ')
    task = input('Input task: ')
    a = [no, deadline, task, 'X']
    todo_list.append(a)


def remove():
    if len(todo_list) == 1:
        print('You have no task to remove.')
        input('\nPress Enter to continue.')
    else:
        for item in todo_list:
            print("{:<5} | {:<10} | {:<20} | {:<5}".format(item[0], item[1], item[2], item[3]))
        a = int(input('\nRemove task number: '))
        if 0 < a < len(todo_list):
            todo_list.pop(a)
            for item in range(1, len(todo_list)):
                b = todo_list[item]
                b[0] = int(item)
                todo_list[item] = b
        else:
            print('\nError. Please try again.')


def save():
    pass


def load():
    pass


def clear():
    if len(todo_list) > 1:
        while len(todo_list) > 1:
            todo_list.pop(1)
        print('Your to-do list is now cleared.')
    else:
        print('Your to-do list has already cleared.')
    input('\nPress Enter to continue.')


def search():
    pass


while True:

    print('\n--- ADVANCE TO-DO APP ---\n\n1. View tasks\n2. Add task\n3. Remove task',
          '\n4. Save tasks\n5. Load tasks\n6. Clear all tasks\n7. Search task',
          '\n8. Exit')

    choice = int(input('\nChoose an option: '))

    if choice == 1:
        view()
    elif choice == 2:
        add()
    elif choice == 3:
        remove()
    elif choice == 4:
        save()
    elif choice == 5:
        load()
    elif choice == 6:
        clear()
    elif choice == 7:
        search()
    elif choice == 8:
        print('Goodbye, see you again.')
        break
    else:
        print('Error. Please try again.')

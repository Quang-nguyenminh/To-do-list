no = 0
deadline = 0
task = 0
a = 0
item = 0
todo_list = [['No.', 'Deadline', 'Task']]


def mark():
    pass


def incomplete():
    pass


def complete():
    pass


def view():
    global item
    for item in todo_list:
        print("{:<5} {:<10} {:<20}".format(item[0], item[1], item[2]))


def add():
    global no
    no = len(todo_list)
    global deadline
    deadline = input('Input deadline: ')
    global task
    task = input('Input task: ')
    global a
    a = [no, deadline, task]
    todo_list.append(a)


def remove():
    global a
    a = int(input('Remove task number: '))
    todo_list.pop(a)
    global item
    for item in range(1, len(todo_list)):
        b = todo_list[item]
        b[0] = int(item)
        todo_list[item] = b


def save():
    pass


def load():
    pass


def clear():
    pass


def search():
    pass


choice = int(input('Choose an option: '))

while choice != 8:

    print('\n--- ADVANCE TO-DO APP ---\n1. View tasks\n2. Add task\n3. Remove task',
          '\n4. Save tasks\n5. Load tasks\n6. Clear all tasks\n7. Search task',
          '\n8. Exit')

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
        break
    else:
        print('nope')

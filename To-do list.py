todo_list = []
complete_tasks = []


def mark():
    pass


def incomplete():
    pass


def complete():
    pass


def view():
    incomplete()
    complete()
    mark()


def add():
    pass


def remv():
    pass


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
          '\n4. Save task\n5. Load task\n6. Clear all task\n7. Search task',
          '\n8. Exit')

    if choice == 1:
        view()
    elif choice == 2:
        add()
    elif choice == 3:
        remv()
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

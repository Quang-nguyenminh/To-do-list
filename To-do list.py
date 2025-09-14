import pandas as pd
todo_list = [['No.', 'Deadline', 'Task', 'Check']]


def mark():
    if len(todo_list) == 1:
        print('You have no task to mark.')
        input('Press Enter to continue.')
    else:
        view()
        print()
        task = int(input('How many tasks do you want to mark: '))
        i = 0
        while i < task:
            a = int(input('Mark task number: '))
            if 0 < a < len(todo_list):
                b = todo_list[a]
                if b[3] == 'X':
                    b[3] = 'O'
                else:
                    b[3] = 'X'
                todo_list[a] = b
                i += 1
            else:
                print('Error. Please try again.')


def view():
    if len(todo_list) == 1:
        print('You have no task on your to-do list.')
    else:
        for item in todo_list:
            print("{:<3}| {:<10}| {:<20}| {:<5}".format(item[0], item[1], item[2], item[3]))
    input('Press Enter to continue.')


def add():
    task = int(input('How many tasks do you want to add: '))
    for i in range(task):
        no = len(todo_list)
        deadline = input('Input deadline: ')
        task = input('Input task: ')
        a = [no, deadline, task, 'X']
        todo_list.append(a)
        print()
    save()


def remove():
    if len(todo_list) == 1:
        print('You have no task to remove.')
        input('\nPress Enter to continue.')
    else:
        view()
        i = 0
        task = int(input('How many tasks do you want to remove: '))
        while i < task:
            r = int(input('\nRemove task number: '))
            if 0 < r < len(todo_list):
                todo_list.pop(r)
                i += 1
                for number in range(1, len(todo_list)):
                    n = todo_list[number]
                    n[0] = number
                    todo_list[number] = n
            else:
                print('\nError. Please try again.')


def save():
    no = []
    deadline = []
    task = []
    check = []
    for i in range(1, len(todo_list)):
        no.append(todo_list[i][0])
        deadline.append(todo_list[i][1])
        task.append(todo_list[i][2])
        check.append(todo_list[i][3])
    df = pd.DataFrame({'No.': no, 'Deadline': deadline, 'Task': task, 'Check': check})
    df.to_csv("To-do list.csv", index=False, encoding='utf-8')


def load():
    df = pd.read_csv("To-do list.csv")
    for v in df:
        todo_list.append(list(df[v]))


def clear():
    i = 1
    if len(todo_list) == 1:
        print('Your to-do list has no task to cleared.')
    else:
        print('What do you want to clear?\n\n1. All completed tasks\n2. All incomplete tasks\n3. All tasks')
        cho = int(input('\nChoose an option:'))
        if cho == 1:
            while i < len(todo_list):
                a = todo_list[i]
                if a[3] == 'O':
                    todo_list.pop(i)
                else:
                    i += 1
            for number in range(1, len(todo_list)):
                n = todo_list[number]
                n[0] = number
                todo_list[number] = n
            print('\nAll completed tasks have been cleared.')
        elif cho == 2:
            while i < len(todo_list):
                a = todo_list[i]
                if a[3] == 'X':
                    todo_list.pop(i)
                else:
                    i += 1
            for number in range(1, len(todo_list)):
                n = todo_list[number]
                n[0] = number
                todo_list[number] = n
            print('\nAll incomplete tasks have been cleared.')
        elif cho == 3:
            while len(todo_list) > 1:
                todo_list.pop(1)
            print('Your to-do list is now cleared.')
        else:
            print('Error. Please try again')
    input('\nPress Enter to continue.')


def search():
    pass


def main():
    load()
    while True:

        print('\n--- ADVANCE TO-DO APP ---\n\n1. View tasks\n2. Add task\n3. Remove task',
              '\n4. Clear tasks\n5. Mark task\n6. Save tasks\n7. Search task',
              '\n8. Exit')

        choice = int(input('\nChoose an option: '))

        if choice == 1:
            view()
        elif choice == 2:
            add()
        elif choice == 3:
            remove()
        elif choice == 4:
            clear()
        elif choice == 5:
            mark()
        elif choice == 6:
            save()
        elif choice == 7:
            search()
        elif choice == 8:
            print('Goodbye, see you again.')
            break
        else:
            print('Error. Please try again.')


if __name__ == '__main__':
    main()
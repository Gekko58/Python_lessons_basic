from os import mkdir, rmdir

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def first_task():
    while True:
        try:
            user_input = int(input("1 - создать папки\n2 - удалить папки\nВведите цифру: "))
            if user_input == 1:
                for index in range(1, 9):
                    try:
                        path = f"dir_{index}"
                        mkdir(path)
                    except OSError:
                        print("Директория существует")
                break
            elif user_input == 2:
                for index in range(1, 9):
                    try:
                        path = f"dir_{index}"
                        rmdir(path)
                    except OSError:
                        print("Директория не существует или не пуста")
                break
            else:
                print("Не верный ввод")
        except ValueError:
            print("Необходимо вводить цифры")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


#Запуск проверки работы программ
try:
    user_input = int(input("Введите номер задачи: "))
    if user_input == 1:
        first_task()
    else:
        print("Не верный ввод. Здесь всего три задачи")
except ValueError:
    print("Не верный ввод")
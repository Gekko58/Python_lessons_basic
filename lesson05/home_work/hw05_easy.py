from os import mkdir, rmdir, listdir, walk, remove
from shutil import copyfile

#Функции для выполнения задания нормал
def create_folder(path):
    try:
        mkdir(path)
        return 0
    except OSError:
        return 1

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def first_task():
    while True:
        try:
            user_input = int(input("1 - создать папки\n2 - удалить папки\nВведите цифру: "))
            if user_input == 1:
                for index in range(1, 10):
                    path = f"dir_{index}"
                    buffer = create_folder(path)
                    if buffer == 1:
                        print("Директория существует")
                        break
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

def second_task():
    directory_list = walk(".")
    print("Список каталогов текущей директории: ")
    for patch, folder_list, file_list in directory_list:
        print(patch)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def third_task():
    try:
        user_input = int(input("1 - скопировать файл\n2 - удалить файл\nВведите цифру: "))
        if user_input == 1:
            copyfile("hw05_easy.py", "hw05_easy.py_backup")
        elif user_input == 2:
            try:
                remove("hw05_easy.py_backup")
            except FileNotFoundError:
                print("Копии файла нет")
        else:
            print("Не верный ввод")
    except ValueError:
        print("Не верный ввод. Необходимо вводить цыфры")

#Запуск проверки работы программ
try:
    user_input = int(input("Введите номер задачи: "))
    if user_input == 1:
        first_task()
    elif user_input == 2:
        second_task()
    elif user_input == 3:
        third_task()
    else:
        print("Не верный ввод. Здесь всего три задачи")
except ValueError:
    print("Не верный ввод, необходимо вводить цыфры")
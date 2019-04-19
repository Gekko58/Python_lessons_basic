from os import mkdir, rmdir, listdir, walk, remove, listdir, chdir
from shutil import copyfile

#Функции для выполнения задания нормал

def change_folder(folder):
    """
    Функция совершает переход в заданную директорию
    :param folder: папка, куда необходимо перейти
    :return: 0 - переход выполнен, 1 - нет такой директории
    """
    try:
        chdir(folder)
        return 0
    except FileNotFoundError:
        return 1

def look_in_folder(mode, folder):
    """
    Функция показывает содержимое директории
    :param mode: 0 - показать только папки, любое другое значение - показать всё сожержимое
    :param folder: папка, содержимое которой необходимо показать
    :return:
    """
    if mode == 0:
        directory_list = walk(folder)
        for patch, folder_list, file_list in directory_list:
            print(patch)
    else:
        print(listdir(folder))
    return None

def delete_folder(path):
    """
    Функция удаляет директорию в текущей папке
    :param path: имя директории
    :return: 0 - если успешно, 1 - если нет такой директории, 2 - если директория не пуста
    """
    try:
        rmdir(path)
        return 0
    except FileNotFoundError:
        return 1
    except OSError:
        return 2

def create_folder(path):
    """
    Функция создаёт диркторию в текущей папке
    :param path: имя создаваемой директории
    :return: 0 если успешно, 1 если директория уже существует
    """
    try:
        mkdir(path)
        return 0
    except FileExistsError:
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
                        print(f"Директория {path} существует")
                break
            elif user_input == 2:
                for index in range(1, 10):
                    path = f"dir_{index}"
                    buffer = delete_folder(path)
                    if buffer == 1:
                        print(f"Директория {path} не существует")
                    elif buffer == 2:
                        print(f"Директория {path} не пуста")
                break
            else:
                print("Не верный ввод")
        except ValueError:
            print("Необходимо вводить цифры")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def second_task():
    print("Список каталогов текущей директории: ")
    look_in_folder(0, ".")

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
if __name__ == "__main__":
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
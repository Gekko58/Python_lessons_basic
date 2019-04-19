from lesson05.home_work.hw05_easy import create_folder

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

try:
    user_input = int(input("Выберите действие:\n"
                       "1. Перейти в папку\n"
                       "2. Просмотреть содержимое текущего каталога\n"
                       "3. Удалить папку\n"
                       "4. Создать папку\n"
                       "Ваше действие: "))
    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        path = input("Введите имя директории: ")
        buffer = create_folder(path)
        if buffer == 0:
            print("Директория успешно создана")
        else:
            print("Директория уже существует")
    else:
        print("Не верный ввод")
except ValueError:
    print("Необходимо вводить цифры")
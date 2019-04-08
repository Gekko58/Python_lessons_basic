# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

def first_task():
    fruits = ["яблоко", "банан", "киви", "арбуз"]
    i = 1
    for index in fruits:
        print('{}. {:*>10}\n'.format(i, index))
        i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def second_task():
    first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    second_list = [1, 3, 5, 7, 9]
    first_set = set(first_list)
    second_set = set(second_list)
    new_set = first_set.difference(second_set)
    first_list = list(new_set)
    print('Значения первого списка без значений из второго: ', first_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

def tree_task():
    first_list = [2, 8, 10, 15, 20, 33, 7, 1, 9, 0]
    new_list = []
    for index in first_list:
        if index % 2 == 0:
            new_list.append(index / 4)
        else:
            new_list.append(index * 2)
    print('Новый лист: ', new_list)

#Запуск задач для проверки
user_input = int(input('Введите номер задачи: '))
if user_input == 1:
    first_task()
elif user_input == 2:
    second_task()
elif user_input == 3:
    tree_task()
else:
    print('Не верный ввод')
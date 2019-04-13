# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    while n <= m:
        a = 1
        b = 1
        for __ in range(n):
            a, b = b, a + b
        print(a)
        n += 1


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    number = 1
    while number < len(origin_list):
        for index in range(len(origin_list) - 1):
            if origin_list[index] > origin_list[index + 1]:
                origin_list[index], origin_list[index + 1] = origin_list[index + 1], origin_list[index]
        number += 1
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def myfilter(function, filter_list):
    output_list = []
    for index in filter_list:
        if function(index) == True:
            output_list.append(index)
    return output_list

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def fourth_task():
    A1 = [1, 3]
    A2 = [4, 7]
    A3 = [2, 8]
    A4 = [-1, 4]
    print('По определению, стороны параллелограмма попарно равны')
    A1A2 = (((A2[0] - A1[0]) ** 2) + ((A2[1] - A1[1]) ** 2)) ** 0.5
    A4A3 = (((A4[0] - A3[0]) ** 2) + ((A4[1] - A3[1]) ** 2)) ** 0.5
    A1A4 = (((A4[0] - A1[0]) ** 2) + ((A4[1] - A1[1]) ** 2)) ** 0.5
    A2A3 = (((A3[0] - A2[0]) ** 2) + ((A3[1] - A2[1]) ** 2)) ** 0.5
    if A1A2 == A4A3 and A2A3 == A1A4:
        print('Это вершины параллелограмма')
    else:
        print('Эти точки не являются вершинами параллелограмма')
    print(f'Длина сторон: A1A2 = {A1A2}, A4A3 = {A4A3}, A1A4 = {A1A4}, A2A3 = {A2A3}')

#Для проверки задач
user_input = int(input('Введите номер задачи: '))
if user_input == 1:
    n = int(input('Введите первое значение ряда: '))
    m = int(input('\nВведите второе значение ряда: '))
    fibonacci(n, m)
elif user_input == 2:
    print('Сортировка массива по возростанию выполнина чуть выше')
elif user_input == 3:
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print('Тестовый массив: ', input_list)
    print('Отфильтруем чётные значения: ')
    print(myfilter((lambda x: x %2 == 0), input_list))
elif user_input == 4:
    fourth_task()
else:
    print('Не верный ввод')
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

input_list = [1, 2, 3, 4, '5', 6, 7, 8, 9, 0]
print(myfilter((lambda x: x == '5'), input_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

n = int(input('Введите первое значение ряда: '))
m = int(input('\nВведите второе значение ряда: '))
fibonacci(n, m)

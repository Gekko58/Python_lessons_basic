import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def first_task():
    input_list = [random.randint(1, 20) for _ in range(10)] #Генерируем произвольный список
    print('Исходный список: ', input_list)
    output_list = [(index ** 2) for index in input_list]
    print(output_list)
    return None

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def second_task():
    source_list = ['яблоко', 'груша', 'апельсин', 'слива', 'персик', 'абрикос', 'дыня', 'арбуз', 'лимон', 'мандарин']
    first_list = [source_list[random.randint(0, len(source_list) - 1)] for _ in range(5)]
    second_list = [source_list[random.randint(0, len(source_list) - 1)] for _ in range(5)]
    print(f"Первый список: {first_list}\nВторой список: {second_list}")
    output_list = set(first_list).union(set(second_list))
    print(f"Общий список фруктов: {output_list}")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def third_task():
    input_list = [random.randint(1, 100) for _ in range(10)]
    print('Исходный список: ', input_list)
    output_list = [index for index in input_list if index % 3 == 0 and index > 0 and index % 4 != 0]
    print('Выходной список: ', output_list)

#Проверка задач
user_input = (input('Введите номер задачи: '))
try:
    user_input = int(user_input)
    if user_input == 1:
        first_task()
    elif user_input == 2:
        second_task()
    elif user_input == 3:
        third_task()
    else:
        print('Не верный ввод')
except ValueError:
    print('Необходимо вводить число')
import random #Для генерации случайных чисел

def random_list(number, beginning, end): #Функция генерирует случайный список из целых чисел
    index = 0
    return_list = []
    while index < number:
        random_number = random.randint(beginning, end)
        return_list.append(random_number)
        index += 1
    return return_list

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def first_task():
    input_list = random_list(30, -100, 100)
    print('Входные данные: ', input_list)
    output_list = []
    for index in input_list:
        toward = abs(index) ** 0.5
        if toward.is_integer():
            toward = int(toward)
            output_list.append(toward)
    print('Результат: ', output_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

def second_task():
    #Словарь дней
    day = {'01': 'Первое',
           '02': 'Второе',
           '03': 'Третье',
           '04': 'Четвёртое',
           '05': 'Пятое',
           '06': 'Шестое',
           '07': 'Седьмое',
           '08': 'Восьмое',
           '09': 'Девятое',
           '10': 'Десятое',
           '11': 'Одинадцатое',
           '12': 'Двенадцатое',
           '13': 'Тринадцатое',
           '14': 'Четырнадцатое',
           '15': 'Пятнадцатое',
           '16': 'Шестнадцатое',
           '17': 'Семнадцатое',
           '18': 'Восемнадцатое',
           '19': 'Девятнадцатое',
           '20': 'Двадцатое',
           '21': 'Двадцать первое',
           '22': 'Двадцать второе',
           '23': 'Двадцать третье',
           '24': 'Двадцать четвёртое',
           '25': 'Двадцать пятое',
           '26': 'Двадцать шестое',
           '27': 'Двадцать седьмое',
           '28': 'Двадцать восьмое',
           '29': 'Двадцать девятое',
           '30': 'Тридцатое',
           '31': 'Тридцать первое',
           }
    month = {'01': 'января',
              '02': 'февраля',
              '03': 'марта',
              '04': 'апреля',
              '05': 'мая',
              '06': 'июня',
              '07': 'июля',
              '08': 'августа',
              '09': 'сентября',
              '10': 'октября',
              '11': 'ноября',
              '12': 'декабря',
               }
    input_date = input('Введите дату: ')
    input_day = day[input_date[0:2]]
    input_month = month[input_date[3:5]]
    input_year = input_date[6:]
    print('Дата: {} {} {} года'.format(input_day, input_month, input_year))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def third_task():
    #Функция генерирования написана в самом начале листинга
    number = int(input('Введите длину генерируемого списка: '))
    print('Выходной список: ', random_list(number, -100, 100))

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def fourth_task():
    #first_list = random_list(10, 1, 4)
    first_list = [1, 2, 4, 5, 6, 2, 5, 2]
    print('Исходный список: ', first_list)
    print('Неповторяющиеся элементы списка: ', set(first_list))

#Запуск задач для проверки
user_input = int(input('Введите номер задачи: '))
if user_input == 1:
    first_task()
elif user_input == 2:
    second_task()
elif user_input == 3:
    third_task()
elif user_input == 4:
    fourth_task()
else:
    print('Не верный ввод')
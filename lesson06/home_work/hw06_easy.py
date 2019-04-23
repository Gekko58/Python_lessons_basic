import random

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    first_coordinate = list()
    second_coordinate = list()
    third_coordinate = list()
    first_segment = float
    second_segment = float
    third_segment = float
    area = float


    def __init__(self, first_coordinate, second_coordinate, third_coordinate):
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate
        self.third_coordinate = third_coordinate

    def area_triangle(self):
        self.first_segment = lenght_segment(self.first_coordinate, self.second_coordinate)
        self.second_segment = lenght_segment(self.second_coordinate, self.third_coordinate)
        self.third_segment = lenght_segment(self.third_coordinate, self.first_coordinate)
        half_meter = (0.5 * (self.first_segment + self.second_segment + self.third_segment))
        self.area = (half_meter * (half_meter - self.first_segment) * (half_meter - self.second_segment) * (half_meter - self.third_segment)) ** 0.5
        print(f"AB = {self.first_segment}\n"
              f"BC = {self.second_segment}\n"
              f"CA = {self.third_segment}\n"
              f"Площадь: {self.area}")

    def altitude_triangle(self):
        print(f"Высота: {(2 * self.area) / self.first_segment}")

    def perimeter_triangle(self):
        print(f"Периметр: {self.first_segment + self.second_segment + self.third_segment}")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    first_coordinate = list()
    second_coordinate = list()
    third_coordinate = list()
    fourth_coordinate = list()
    first_segment = float
    second_segment = float
    third_segment = float
    fourth_segment = float
    first_diagonal = float
    second_diagonal = float
    def __init__(self, first_coordinate, second_coordinate, third_coordinate, fourth_coordinate):
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate
        self.third_coordinate = third_coordinate
        self.fourth_coordinate = fourth_coordinate
        self.first_segment = lenght_segment(first_coordinate, second_coordinate)
        self.second_segment = lenght_segment(second_coordinate, third_coordinate)
        self.third_segment = lenght_segment(third_coordinate, fourth_coordinate)
        self.fourth_segment = lenght_segment(fourth_coordinate, first_coordinate)
        self.first_diagonal = lenght_segment(first_coordinate, third_coordinate)
        self.second_diagonal = lenght_segment(second_coordinate, fourth_coordinate)
        print(f"AB = {self.first_segment}\n"
              f"BC = {self.second_segment}\n"
              f"CD = {self.third_segment}\n"
              f"DA = {self.fourth_segment}\n"
              f"AC = {self.first_diagonal}\n"
              f"BD = {self.second_diagonal}")

    def isosceles(self):
        if self.first_diagonal == self.second_diagonal:
            return 1

    def perimetr_trapeze(self):
        print(f"Периметр: {self.first_segment + self.second_segment + self. third_segment + self.fourth_segment}")

    def area_trapez(self):
        first_element = (self.first_segment + self.second_segment) / 2
        second_element = (((self.second_segment - self.first_segment) ** 2 + self.third_segment ** 2 - self.fourth_segment ** 2) / (2 * (self.second_segment - self.first_segment))) ** 2
        third_element = (self.third_segment ** 2 - second_element) ** 0.5
        area = first_element * third_element
        print(f"Площадь: {area}")

#Функции генерации координат и подсчёта длины отрезка
def generate_coordinate():
    return_list = []
    return_list.append(random.randint(-10, 10))
    return_list.append(random.randint(-10, 10))
    return return_list

def lenght_segment(first_coordinate, second_coordinate):
    lenght = (((second_coordinate[1] - first_coordinate[1]) ** 2 + (second_coordinate[0] - first_coordinate[0]) ** 2) ** 0.5)
    return lenght

#Запуск проверки работы программы
if __name__ == "__main__":
    def first_task():
        first_coordinate = generate_coordinate()
        second_coordinate = generate_coordinate()
        third_coordinate = generate_coordinate()
        print(f"Координаты треугольника: {first_coordinate}, {second_coordinate}, {third_coordinate}")
        triangle = Triangle(first_coordinate, second_coordinate, third_coordinate)
        triangle.area_triangle()
        triangle.altitude_triangle()
        triangle.perimeter_triangle()

    def second_task():
        first_coordinate = generate_coordinate()
        second_coordinate = generate_coordinate()
        third_coordinate = generate_coordinate()
        fourth_coordinate = generate_coordinate()
        print(f"Координаты трапеции: {first_coordinate} {second_coordinate} {third_coordinate} {fourth_coordinate}")
        trapeze = Trapeze(first_coordinate, second_coordinate, third_coordinate, fourth_coordinate)
        if trapeze.isosceles() == 1:
            print("Равнобедренная трапеция")
        else:
            print("Не равнобедренная трапеция")
        trapeze.perimetr_trapeze()
        trapeze.area_trapez()

    task_start = {1: first_task,
                  2: second_task,
                  }
    try:
        user_input = int(input("Введите номер задачи: "))
        if user_input == 1:
            task_start[1]()
        elif user_input == 2:
            task_start[2]()
        else:
            print("Не верный ввод")
    except ValueError:
        print("Вводить необходимо цифры")
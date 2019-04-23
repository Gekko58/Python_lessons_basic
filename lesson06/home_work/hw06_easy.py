import random

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    first_coordinate = list()
    second_coordinate = list()
    third_coordinate = list()

    def __init__(self, first_coordinate, second_coordinate, third_coordinate):
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate
        self.third_coordinate = third_coordinate

    def lenght_segment(self, first_coordinate, second_coordinate):
        lenght = (((second_coordinate[1] - first_coordinate[1]) ** 2 + (second_coordinate[0] - first_coordinate[0]) ** 2) ** 0.5)
        return lenght

    def area_triangle(self):
        first_segment = self.lenght_segment(self.first_coordinate, self.second_coordinate)
        second_segment = self.lenght_segment(self.second_coordinate, self.third_coordinate)
        third_segment = self.lenght_segment(self.third_coordinate, self.first_coordinate)
        half_meter = (0.5 * (first_segment + second_segment + third_segment))
        area = (half_meter * (half_meter - first_segment) * (half_meter - second_segment) * (half_meter - third_segment)) ** 0.5
        print(f"AB = {first_segment}\n"
              f"BC = {second_segment}\n"
              f"CA = {third_segment}\n"
              f"Площадь: {area}")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

def generate_coordinate():
    return_list = []
    return_list.append(random.randint(-10, 10))
    return_list.append(random.randint(-10, 10))
    return return_list

#Запуск проверки работы программы
if __name__ == "__main__":
    def first_task():
        first_coordinate = generate_coordinate()
        second_coordinate = generate_coordinate()
        third_coordinate = generate_coordinate()
        print(f"Координаты треугольника: {first_coordinate}, {second_coordinate}, {third_coordinate}")

        triangle = Triangle(first_coordinate, second_coordinate, third_coordinate)
        triangle.area_triangle()

    task_start = {1: first_task,
                  }
    try:
        user_input = int(input("Введите номер задачи: "))
        if user_input == 1:
            task_start[1]()
    except ValueError:
        print("Вводить необходимо цифры")
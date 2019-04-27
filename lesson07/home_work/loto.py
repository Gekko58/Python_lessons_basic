#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Barels:
    bug = []
    selected_barell = 0
    def __init__(self):
        self.bug = self.filling_bag()

    def filling_bag(self):
        return_bug = []
        for index in range(1, 91):
            return_bug.append(index)
        return return_bug

    def choose_barel(self):
        if self.selected_barell == 0:
            self.selected_barell = random.choice(self.bug)
        else:
            self.bug.remove(self.selected_barell)
            self.selected_barell = random.choice(self.bug)

class Card:
    def __init__(self):
        self.first_string = self.generate_string()
        self.second_string = self.generate_string()
        self.tree_string = self.generate_string()

    def generate_string(self):
        string = []
        for _ in range(9):
            string.append("")
        index = 0
        while index < 5:
            cell_number = random.randint(0, 8)
            if string[cell_number] == "":
                string[cell_number] = random.randint(1, 91)
                index += 1
        return string

    def print_string(self, string):
        output_string = ""
        for index in string:
            output_string = output_string + str(index) + " "
        print(output_string)

    def print_card(self):
        self.print_string(self.first_string)
        self.print_string(self.second_string)
        self.print_string(self.tree_string)

    def find_number(self, string, number):
        try:
            index = string.index(number)
            string[index] = "-"
        except ValueError:
            return 0

    def check_win(self):
        if self.first_string.count("-") == 5\
        and self.second_string.count("-") == 5 \
        and self.tree_string.count("-") == 5: \
            return 0

    def find_number_card(self, number):
        check_first_string = self.find_number(self.first_string, number)
        check_second_string = self.find_number(self.second_string, number)
        check_tree_string = self.find_number(self.tree_string, number)
        if check_first_string == 0 and check_second_string == 0 and check_tree_string == 0:
            return 0

if __name__ == "__main__":
    input_user = ''
    barels = Barels()
    gamer_card = Card()
    comp_card = Card()
    while True:
        barels.choose_barel()
        print(f"Новый бочёнок: {barels.selected_barell} (осталось {len(barels.bug)})")
        print("----Ваша карточка-----")
        gamer_card.print_card()
        print("----------------------")
        print("--Карточка комьютера--")
        comp_card.print_card()
        print("----------------------")
        input_user = input("Зачеркнуть?(Y/N)")
        if input_user == 'y':
            if gamer_card.find_number_card(barels.selected_barell) == 0:
                print("У вас в карточке нет такого значения. Конец игры")
                break
            else:
                comp_card.find_number_card(barels.selected_barell)
        elif input_user == 'n':
            if gamer_card.find_number_card(barels.selected_barell) != 0:
                print("У вас в карточке есть такое значение, вы ошиблись. Конец игры")
                break
            else:
                comp_card.find_number_card(barels.selected_barell)
        else:
            print("Неверный ввод, выход")
            break
        if gamer_card.check_win() == 0:
            print("Поздравляю, вы выиграли!")
        if comp_card.check_win() == 0:
            print("Вы проиграли. Компьютер закрыл все значения")
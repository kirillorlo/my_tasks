import random

"""
Вы пришли на работу в компанию по разработке игр, целевая аудитория —
дети и их родители. У предыдущего программиста было задание сделать две
игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не
успел выполнить эту задачу и оставил только небольшой шаблон проекта.
Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
число».
Правила игры «Камень, ножницы, бумага»: программа запрашивает у
пользователя строку и выводит, победил он или проиграл. Камень бьёт
ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число
до тех пор, пока он не отгадает загаданное.
def rock_paper_scissors():
# Здесь будет игра «Камень, ножницы, бумага»
def guess_the_number():
# Здесь будет игра «Угадай число»
def mainMenu():
# Здесь главное меню игры
mainMenu():
pass
"""


def rock_paper_scissors():
    while True:
        subject = int(input('select an item: 1 - камень, 2 - ножницы, 3 - бумага, 4 - выход '))
        if subject == 4:
            main_menu()
            break
        computer = random.choice(range(1, 4))
        print(f'Компьютер выбрал: {computer}')
        if subject == computer:
            print('Ничья')
        elif subject > computer:
            print('Вы выиграли!')
        elif subject < computer:
            print('Вы проиграли!')
        else:
            break


def guess_the_number():
    computer = random.choice(range(1, 11))
    while True:
        number = int(input('Введите число от 1 до 10 - '))
        if number == -1:
            main_menu()
        print(f'Компьютер выбрал: {computer}')
        if number == computer:
            print('Вы угадали!)')
            break
        elif number != computer:
            print('Неверное число, попробуйте снова!')


def main_menu():
    while True:
        choose = int(input("Выберете действие: 1 - игра 'Камень, ножницы, бумага', 2 - игра 'Угадай число', 3 - выход "))
        if choose == 1:
            rock_paper_scissors()
        elif choose == 2:
            guess_the_number()
        else:
            print('Вы вышли из меню!')
            break


main_menu()

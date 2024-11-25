"""
Апгрейд калькулятора
Степан использует калькулятор для расчёта суммы и разности чисел, но на
работе ему требуются не только обычные арифметические действия. Он ничего
не хочет делать вручную, поэтому решил немного расширить функционал
калькулятора.
Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или
минимальную цифру. Каждое действие оформите в виде отдельной функции, а
основную программу зациклите.
Запрошенные числа должны передаваться в функции суммы, максимума и
минимума при помощи аргументов.
"""


def sum_numbers(numbers):
    numbers = [int(x) for x in numbers]
    return sum(numbers)


def max_numbers(numbers):
    numbers = [int(x) for x in numbers]
    return max(numbers)


def min_numbers(numbers):
    numbers = [int(x) for x in numbers]
    return min(numbers)


while True:
    numbers = input('Enter number: ')
    action = int(input('Choose an action: 1 - sum of digits, 2 - minimum number, 3 - maximum number: '))

    if action == 1:
        print(sum_numbers(numbers))
    elif action == 2:
        print(max_numbers(numbers))
    elif action == 3:
        print(min_numbers(numbers))
    else:
        print('Invalid command')

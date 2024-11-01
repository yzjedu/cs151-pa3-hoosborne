# Programmers: Hazel Osborne
# Course:  CS151, Dr. Zee
# Due Date: 10/30/2024
# Lab Assignment: PA 3
# Problem: creating a program to display ASCII art and string decorations to the user.
# Credits: Design 3 -> Shanaka Dias

import random

#Purpose: Take user choice for type of ASCII art.
#Name: user_choice_input
#Parameters: none
#Return: choice
def user_choice_input():
    print('Choose whether you would like to pick a random pre-made ASCII art, a custom field of a specific character, or a circle')
    choice = input("Please enter random, custom, or circle: ")
    choice = choice.lower()
    #Error Correction
    while choice != 'random' and choice != 'custom' and choice != 'circle':
        choice = input("Invalid Input. Please enter random, custom, or circle: ")
        choice = choice.lower()
    return choice

#Purpose: randomly generate an integer to pick a random design
#Name: random_design_generate
#Parameters: none
#Return: none
def random_design_generate():
    random_int = random.randint(1, 3)
    if random_int == 1:
        print_design_1()
    elif random_int == 2:
        print_design_2()
    elif random_int == 3:
        print_design_3()
    return
#Purpose: print out 1st random design
#Name: print_design_1
#Parameters: none
#Return: none
def print_design_1():
    print('\n')
    print(f'{"^      ^":^10}')
    print(f'{"(  \\__/  )":^10}')
    print(f'{"[  0  0  ]   $":^10}')
    print(f'{"/  \\/  \\   /":^14}')
    print(f'{"/_u____u_\\ /":^10}')
    print(f'{"0        0":^10}')
    print('You got design 1!')
    print('\n', '~'*100)
    return

#Purpose: print out 2nd random design
#Name: print_design_2
#Parameters: none
#Return: none
def print_design_2():
    print('\n')
    print(f'{"_____":^10}')
    print(f'{"_|___|_   %":^14}')
    print(f'{"(( ^_^ )) /":^10}')
    print(f'{"__/   \\__/":^10}')
    print(f'{"/_____\\":^10}')
    print(f'{"_|   |_":^10}')
    print('You got design 2!')
    print('\n', '~'*100)
    return

#Purpose: print out 3rd random design
#Name: print_design_3
#Parameters: none
#Return: none
def print_design_3():
    print('\n')
    print(f'{"_\\/_":^12}')
    print(f'{"/\\":^12}')
    print(f'{"/\\":^12}')
    print(f'{"/  \\":^12}')
    print(f'{"/~~\\o":^12}')
    print(f'{"/o   \\":^12}')
    print(f'{"/~~*~~~\\":^12}')
    print(f'{"o/    o \\":^12}')
    print(f'{"/~~~~~~~~\\":^12}')
    print(f'{"/__*_______\\":^10}')
    print(f'{"||":^12}')
    print('You got design 3!')
    print('\n', '~'*100)
    return

#Purpose: Print a circle
#Name: circle_print
#Parameters: none
#Return: choice
def circle_print():
    circle_list = [6, 12, 14, 14, 12, 6]
    print('\n')
    for num in circle_list:
        print(f'{"*"*num:^20}')
    print('\n', '~'*100)
    return

#Purpose: check if a variable is a valid integer
#Name: error_check_int
#Parameters: amount
#Return: amount
def error_check_int(amount):
    while not amount.isdigit() :
        amount = input("Please enter a valid integer: ")
    amount = int(amount)
    while amount < 0:
        amount = input("Please enter a valid integer: ")
    amount = int(amount)
    return amount

#Purpose: collect and output user custom design
#Name: user_custom_input
#Parameters: none
#Return: none
def user_custom_input():
    count = 0
    character = str(input("Please enter the character you would like to use for your art: "))
    columns = input('Please enter how many columns you would like there to be: ')
    columns = error_check_int(columns)
    rows = input('Please enter how many rows you would like there to be: ')
    print('~'*100)
    rows = error_check_int(rows)
    print('\n')
    while count < rows:
        print(character * columns)
        count += 1
    print('\n')
    print('~'*100)
    return

#Purpose: display ASCII art and string decorations to the user.
#Name: Main
#Parameters: none
#Return: none
def main():
    print('\n', '~'*100)
    print("Welcome to the ASCII art Generator!!! \n Credit to Shanaka Dias for Design 3!")
    print('~'*100, '\n')
    continue_choice = ''
    while continue_choice != 'no':
        user_choice = user_choice_input()
        if user_choice == 'random':
            random_design_generate()
        elif user_choice == 'circle':
            circle_print()
        elif user_choice == 'custom':
            user_custom_input()
        continue_choice = input('Would you like to go again? \n Yes or No: ')
        while continue_choice != "no" and continue_choice != 'yes':
            continue_choice = input('Invalid Input. Yes or No: ')
    print('~'*100)
    print('\n Thanks for using the ASCII art generator!!!')


main()
import random


def initialize_score(identifier):
    file = open('rating.txt', 'r')
    for line in file:
        line = line.replace('\n', '')
        words = line.split()
        if words[0].lower() == identifier.lower():
            file.close()
            return int(words[1])
    file.close()
    return 0


def game_options():
    user_input = input()
    return ['rock', 'paper', 'scissors'] if user_input == '' else user_input.split(',')


def winning_cases(options_list):
    winning_cases_dict = {}
    for element in options_list:
        # Place element in the middle of the list of options
        num_rotations = len(options_list) // 2 - options_list.index(element)
        options_list = options_list[-num_rotations:] + options_list[:-num_rotations]
        # One element wins over one-half of the remaining ones and loses to the other
        winning_cases_dict[element] = options_list[len(options_list) // 2 + 1:]
    return winning_cases_dict


def get_choices():
    user = input()
    computer = random.choice(options)
    return user, computer


def determine_outcome(user, computer):
    if user == computer:
        return 'DRAW'
    if user in wins_against[computer]:
        return 'WIN'
    return 'LOSE'


def message(outcome, computer):
    return {'DRAW': f'There is a draw ({computer})',
            'WIN': f'Well done. The computer chose {computer} and failed',
            'LOSE': f'Sorry, but the computer chose {computer}'}[outcome]


def update_score(outcome, user_score):
    add_to_score = {'DRAW': 50, 'WIN': 100, 'LOSE': 0}
    return user_score + add_to_score[outcome]


name = input('Enter your name: ')
print('Hello,', name)

score = initialize_score(name)

options = game_options()
wins_against = winning_cases(options)

print("Okay, let's start")
user_choice, computer_choice = get_choices()
while user_choice != '!exit':
    if user_choice in options:
        result = determine_outcome(user=user_choice, computer=computer_choice)  # WIN, LOSE OR DRAW
        print(message(result, computer_choice))
        score = update_score(result, score)
    elif user_choice == '!rating':
        print('Your rating:', score)
    else:
        print('Invalid input')
    user_choice, computer_choice = get_choices()

print('Bye!')

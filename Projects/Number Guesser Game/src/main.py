import random
from termcolor import colored
from src.utils.input_validator import validate_input


def main():
    random_number = random.randint(1, 100)
    score = 100

    while score:
        user_guess = input('Guess a number between 1 to 100: ')

        if user_guess == "q":
            print(colored('Thank you for playing. Goodby!', 'yellow', attrs=['bold']))
            break

        if not validate_input(user_guess):
            continue
        
        user_guess = int(user_guess)
        if user_guess > random_number:
            print(colored(f'The number is less than {user_guess}.', 'red',  attrs=['bold']))

        elif user_guess < random_number:
            print(colored(f'The number is grather than {user_guess}.', 'red',  attrs=['bold']))

        else:
            print(colored(f'Congragelations you win!\nYour score is: {score}.', 'green',  attrs=['bold']))
            wanna_play = input('Do you want to play again? (y/n)')
            if wanna_play == 'y':
                random_number = random.randint(1, 100)
                score = 100
                continue
            else:
                print(colored('Good by!', 'green', attrs=['bold']))
                break
        
        score -= 10
        score = max(0, score)

    else:
        print(colored(f'Game over! The number was {random_number}', 'red', attrs=['bold']))


if __name__ == '__main__':
    main()


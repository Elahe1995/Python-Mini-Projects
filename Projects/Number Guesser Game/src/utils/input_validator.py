from termcolor import colored

def validate_input(user_guess):
    if not user_guess.isdigit():
        print(colored('Invalid input. Please try again.', 'red', attrs=['bold'])) 
        return False

    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > 100:
        print(colored('Your guess is out of range. Your guess should be between 1 to 100. Please try again.', 'red',  attrs=['bold']))
        return False
    
    return True

if __name__ == '__main__':
    print(validate_input('25'))
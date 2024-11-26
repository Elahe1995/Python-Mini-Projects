import random

class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f'enter your choice {self.choices}')
        if user_choice.lower() in self.choices:
            return user_choice
        
        print(f'Invalid choice, you must select from {self.choices}')
        return self.get_player_choice()
    
    def get_computer_choice(self):
        return  random.choice(self.choices)
    
    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        win_combinations = [('scissors', 'paper'), ('rock', 'scissors'), ('paper', 'rock')]
        for win_com in win_combinations:
            if (user_choice == win_com[0]) & (computer_choice == win_com[1]):
                return "Congaratulatons! you won!"
            
        return "Oh no! The computer won!"
    
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'Computer_choice: {computer_choice}')
        print(self.decide_winner(user_choice, computer_choice))

if __name__ == '__main__':
    game = RockPaperScissors('Elahe')

    while True:
        game.play()

        continue_game = input("Do you want to play again? (enter any key to continue and q/Q to exit!)")
        if continue_game.lower() == 'q':
            break
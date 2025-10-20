import random

class NumberGuessingGame:
    def __init__(self):
        self.unknown_number = random.randint(1, 100)
        self.attempt = 0
    
    def check_guess(self, guess):
        self.attempt = self.attempt + 1
        
        if guess < self.unknown_number:
            return -1
        elif guess > self.unknown_number:
            return 1
        else:
            return 0
    
    def play(self):
        print("Welcome to Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        
        while True:
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            
            result = self.check_guess(guess)
            
            if result == -1:
                print("a little low! Try again.")
            elif result == 1:
                print("a little high! Try again.")
            else:
                print("Congratulations! You found the number!")
                print(f"You found it in {str(self.attempt)} attempts.")
                break

game = NumberGuessingGame()
game.play()
from random import choice
word_list = ["Interstellar",
                   "The GodFather",
                   "Inception",
                   "The Matrix",
                   "Pulp Fiction"]

class Hangman():
    def __init__(self,word_list,num_lives=5) -> None:
        self.word = choice(word_list)
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again')
            print(f'You have {self.num_lives} lives left')


    def ask_for_input(self):
        while True:
            guess = input("Please, enter a single alphabetical character")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    print(game.word)
    while True:
        if num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            print(game.num_letters)
            print(game.word_guessed)
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")

play_game(word_list)
from random import choice

class Hangman:
    def __init__(self, words, lives=5):
        """Initialize the Hangman game with a random word and set the initial game state."""
        self._word = choice(words).lower()  # Use _ to indicate a protected member
        self._word_display = self._initialize_word_display(self._word)
        self._remaining_unique_letters = self._count_unique_letters(self._word)
        self._lives = lives
        self._guessed_letters = set()

    def _initialize_word_display(self, word):
        """Create the initial display of the word with underscores and spaces."""
        return ['_' if char != ' ' else ' ' for char in word]

    def _count_unique_letters(self, word):
        """Count the number of unique letters in the word, ignoring spaces."""
        return len(set(char for char in word if char.isalpha()))

    def _is_valid_guess(self, guess):
        """Check if the guess is a single alphabetical character."""
        return len(guess) == 1 and guess.isalpha()

    def _update_word_display(self, guess):
        """Update the display of the word with the correct guessed letter."""
        for i, char in enumerate(self._word):
            if char == guess:
                self._word_display[i] = guess

    def _process_guess(self, guess):
        """Process the player's guess and update the game state."""
        if guess in self._word:
            self._update_word_display(guess)
            self._remaining_unique_letters -= 1
            print(f'Good guess! {guess} is in the word.')
        else:
            self._lives -= 1
            print(f'Sorry, {guess} is not in the word. You have {self._lives} lives left.')

    def _is_game_over(self):
        """Check if the game is over due to loss of lives or successful guessing."""
        if self._lives <= 0:
            print("You lost!")
            return True
        elif self._remaining_unique_letters == 0:
            print("Congratulations! You've guessed the word!")
            return True
        return False

    def _get_guess(self):
        """Prompt the user for a guess, ensuring it's valid and hasn't been guessed before."""
        while True:
            guess = input("Please enter a single alphabetical character: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self._guessed_letters:
                print("You have already guessed that letter.")
            else:
                self._guessed_letters.add(guess)
                return guess

    def play(self):
        """Main game loop, handling the flow of the Hangman game."""
        while not self._is_game_over():
            print(' '.join(self._word_display))
            guess = self._get_guess()
            self._process_guess(guess)

def start_game(word_list):
    """Start a new Hangman game with the provided list of words."""
    game = Hangman(word_list)
    game.play()

word_list = ["Interstellar", "The GodFather", "Inception", "The Matrix", "Pulp Fiction"]
start_game(word_list)
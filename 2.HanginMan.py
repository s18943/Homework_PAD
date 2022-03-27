from random import choice
from math import floor
import sys
from pip import main

class Hang:
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
        'coyote crow deer dog donkey duck eagle ferret fox frog goat '
        'goose hawk lion lizard llama mole monkey moose mouse mule newt '
        'otter owl panda parrot pigeon python rabbit ram rat raven '
        'rhino salmon seal shark sheep skunk sloth snake spider '
        'stork swan tiger toad trout turkey turtle weasel whale wolf '
        'wombat zebra ').split()

    HANGMANPICS = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']


class Game:

    def __init__(self, players=1):
        self.players = players

    def _play(self):
        print("Game begins NOW")
        print(f"Players: {self.players}")

class Hangman(Game):
    difficalty_dict = {'beginner': 8, 'intermediate': 5,'advanced': 3}
    difficalty_curr = 'beginner'
    attempts = 8

    def __init__(self, players):
        super().__init__(players)

        difficalty_list = list(self.difficalty_dict.keys())
        [print(str(i+1) + ". " + difficalty_list[i]) for i in range(len(difficalty_list))]
        user_pick = int(input())-1
        self.difficalty_curr = difficalty_list[user_pick]
        self.attempts = self.difficalty_dict.get(self.difficalty_curr)
        print(self.players)
        if self.players > 1:
            self.the_word = "27"
            while not self.the_word.isalpha() or len(self.the_word) < 3:
                self.the_word = input("Wymyśl slowo dla przeciwnika: ")
                if not self.the_word.isalpha():
                    print("only alphabethic characters please")
                if len(self.the_word) < 3:
                    print("try a bit longer word")
        else:
            self.the_word = choice(Hang.words)

                
            
        self._play()

    def _play(self):
        super()._play() 
        print(f"Difficalty: {self.difficalty_curr}")
        self._main_loop()

    def check_loss(self):
        flag = True
        if self.attempts <= 0:
            flag = False
            print("""Sorry, that is the END!""")
        return flag

    def next_pick(self, att):
        curr_dif = self.difficalty_dict.get(self.difficalty_curr)
        prop = len(Hang.HANGMANPICS)/curr_dif
        att = curr_dif - att + 1 
        n = floor(att*prop) - 1 
        n = n if n > 0 else 0 
        print(Hang.HANGMANPICS[n])

    def win(self):
        print(f'Yes the word is "{self.the_word}"')
        print("Great job! You WON!")

    def _main_loop(self):
        flag = True
        guessed = set()
        attemts = set()
        displayed_word = ''.join(['-' for i in self.the_word])

        while flag:
            print(displayed_word)
            player_gues = input("Put one Letter: ").lower()
            if player_gues.isalpha():
                if len(player_gues)==1:
                    if player_gues in self.the_word:
                        print("There is such letter!")
                        guessed.add(player_gues)
                        displayed_word = ''.join(['-' if (i not in guessed) else i for i in self.the_word ])
                        if '-' not in displayed_word:
                            flag = False
                            self.win()

                    elif player_gues not in attemts:
                        self.next_pick(self.attempts)
                        self.attempts -= 1
                        print("There is no such letter")
                        flag = self.check_loss()

                    else:    
                        print('You already tryed this letter')

                    attemts.add(player_gues)                
                    print()
                elif len(player_gues)==len(self.the_word):
                    if player_gues==self.the_word:
                            flag = False
                            self.win()
                    else:
                        print("Nope, that is not the word")
                        flag = self.check_loss()

                else:
                    print("Your guess is not legit - not a full word or single letter")
            else:
                print("Your guess is not legit - it contains non alpha characters")


def main() -> int:
    hang_game = Hangman(int(input("How many players ?: ")))
    return 0

if __name__ == '__main__':
    sys.exit(main())


import random
import hangman_arts
import hangman_words
from os import system

def hangman():

  print(hangman_arts.logo)

  print("Welcome to the Hangman Game!")
  word_list = hangman_words.word_list
  random_choice = random.choice(word_list)
  list_letters = [l for l in random_choice]
  print(list_letters)
  empty_string = ['_' for i in random_choice]
  print(empty_string)
  end_of_game = False
  word_len = len(list_letters)
  lives = 6

  while not end_of_game:
    user_choice = input("Please guess a letter!\n").lower()
    system('clear')
    print(hangman_arts.stages[-1])
    if user_choice in empty_string:
      print(f"You have already guessed {user_choice}")
      
    for position in range(word_len):
      if user_choice == list_letters[position]:
        empty_string[position] = user_choice
        print(empty_string)

    if '_' not in empty_string:
        end_of_game = True
        print("You win!")

    if user_choice not in list_letters:
      print(f"You guessed the {user_choice}, which doesn't existe in the word, so you lose a live.")
      lives -= 1
      print(hangman_arts.stages[lives])
      
      if lives == 0:
          end_of_game = True
          print("You lose!")




if __name__ == "__main__":
    hangman()
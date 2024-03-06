import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False 
lifes = 6

from hangman_art import logo
print(logo)

#print(f"Shhhh, the correct word is: {chosen_word}")

exhibition = []

for _ in range(word_length):
  exhibition += "_"

while not game_over:
  guess = input("Take a guess:\n").lower()
  
  if guess in exhibition:
    print(f"You already guessed: {guess}.\n")

  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
      exhibition[position] = letter

  if guess not in chosen_word:
    print(
      f"You guessed: {guess}, that's not in the word, you lose 1 life."
    )
    lifes -= 1 #lifes = lifes - 1

    if lifes == 0:
      game_over = True
      print("Game Over!")

  print(f"{' '.join(exhibition)}")

  if "_" not in exhibition:
    game_over = True 
    print("You win!")

  from hangman_art import stages
  print(stages[lifes])
  
  
  
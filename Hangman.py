import random

#Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

#Choose a random word and initialise variables 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Logo printing 
from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks and check for repetition of letters 
display = []
all_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in all_letters:
      print(f"You have already entered {guess}. Try something else.")
      continue
    else:
      all_letters.append(guess)

    #Check guessed letter and edit display accordingly
    for position in range(word_length):
        letter = chosen_word[position]
       #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") - testing 
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was '{chosen_word}'")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f"The word was {chosen_word}.")

    #Import the stages from hangman_art.py 
    from hangman_art import stages
    print(stages[lives])

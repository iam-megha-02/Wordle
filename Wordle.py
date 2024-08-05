import random

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
reset = '\033[0m'

word_bank = []

try:
    with open("word_bank.txt") as word_file:
        for line in word_file:
            word_bank.append(line.rstrip().lower())

except FileNotFoundError:
    exit()

if not word_bank:
    exit()

guess_word = random.choice(word_bank)


misplaced_ltr = []
wrong_ltr = []
max_turns = 5
turns_taken = 1

print(f"Welcome to Wordle!\nThe word you have to guess is of {len(guess_word)} letters.\
      \nYou have {max_turns} chances to guess the word.\nLet's Start!!")


while turns_taken <= max_turns:

    user_guess = input("Guess a word: ").lower()

    if len(user_guess) != len(guess_word) or not user_guess.isalpha():
        print("Please enter 6-letter word.")
        continue

    i = 0

    for w in user_guess:

        if w == guess_word[i]:
            print(f"{green}{w}{reset}",end=" ")
            if w in misplaced_ltr:
                misplaced_ltr.remove(w)
        

        elif w in guess_word:
            if w not in misplaced_ltr:
                misplaced_ltr.append(w)
            print(f"{yellow}{w}{reset}",end=" ")

        else:
            if w not in wrong_ltr:
                wrong_ltr.append(w)
            print(f"{red}{w}{reset}",end=" ")
        
        i+=1

    if user_guess == guess_word:
        print("\nBravo! You guessed it right.")
        break

    if turns_taken==max_turns:
        print("\nYou are out of turns!")
        break

    print(f"\nYou have {max_turns-turns_taken} chances left!")   

    turns_taken+=1





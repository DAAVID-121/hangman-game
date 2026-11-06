import random
random_words = ["python", "program", "calculator", "database", "computer", "internet", "notebook", "keyboard", "football"]
while True:
    word = random.choice(random_words)
    lives = 6
    guessed_letters = []
    tried_letters = []  
    print("Welcome to the Word Guessing Game! I will choose a word for you to guess. You will have 6 attempts to guess the words letters correctly.")
    ready = input("Are you ready to start? yes/no: ").lower()
    if ready == "yes":
        while True:
            display_word = ""
            for guess in word:
                if guess in guessed_letters:
                    display_word += guess + " "
                else:
                    display_word += "_ "
            print(f"{display_word} | Lives left: {lives} | Tried letters: {', '.join(tried_letters)}")
            if "_" not in display_word:
                print(f"Congratulations! You guessed the word '{word}' correctly!")
                break
            letter = input("Enter a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha(): 
                print("Please enter a single letter.")
                continue
            if letter in tried_letters:
                print(f"you have tried the letter '{letter}' before. Please try a different letter.")
                continue
            tried_letters.append(letter)
            if letter in word:
                guessed_letters.append(letter)
                print(f"Good guess! The letter '{letter}' is in the word.")
            else:
                lives -= 1
                print(f"Sorry, the letter '{letter}' is not in the word. You have {lives} lives left.")
            if lives == 0:
                print(f"You lost! The word was '{word}'.")
                break        
    elif ready == "no":
        print("Goodbye!")
        break
    else :
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue 
    print("Do you want to play again? (yes/no)")
    play_again = input().lower()
    if play_again != "yes":
        print("All right, goodbye!")
        break
 




    
    
        
        
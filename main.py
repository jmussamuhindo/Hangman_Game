import random
from hangman_word import word_list
from hangman_art import logo, stages



chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

#Create a variable called 'lives' to keep track ot the number of lives left.
# #testing_code
#Set 'lives' to equal 6.
lives = 6

print(logo)

#Testing code
# print(f"Please, the solution is {chosen_word}")

#create a blank list
display = []

for _ in range(word_lenght):
    display +="_"

end_of_game = False

while not end_of_game :
    guess = input("Guess a letter: ").lower()
    
    #If the user has entered a letter the've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    

    #check guesssed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Gussed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    #if guess is not a letter in the chosen_word, 
    #then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "you win"
    if guess not in chosen_word:
        #- If the letter is not in the chosen_word, print out the leter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    #join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    #Print the ASCII art from 'stages that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
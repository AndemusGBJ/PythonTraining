'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

givenWord="java"
givenWord = list(givenWord)
guessedWord=[]

for i in range(len(givenWord)):
    guessedWord += "_"

    
used_letters = []
rounds=6

while rounds != 0:
    print("")
    print(f"You have {rounds} tries left.")
    print(f"Used letters: {' '.join(used_letters)}")
        
    print(f"Word: {' '.join(guessedWord)}")
    
    player = input("Guess a letter: ")
    
    
    for i in range(len(givenWord)):
        if givenWord[i] == player:
            guessedWord[i] = player
    
    if guessedWord == givenWord:
        print(f"You guessed the word {''.join(guessedWord)} !")
        break
        
    used_letters += player
        
    
    rounds -=1
    
if guessedWord != givenWord:
    print("You have lost !")



"""
Dan by Albert Gubanja

"""


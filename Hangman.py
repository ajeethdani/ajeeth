#word_list=["adani","baboon","camel"]
import random
from word_list import word_list


# logo = [''' 
#  _                                             
# | |                                            
# | |_   _ _ _ _   _ _ _ _ __   _ _ _ _  
# | '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
# | | | | (| | | | | (| | | | | | | (_| | | | |
# || ||\_,|| ||\_, || || ||\_,|| ||
#                     __/ |                      
#                    |_/ 
# ''']
# print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word=random.choice(word_list)

lives=6

display=[]
for i in chosen_word:
    display+=["_"]
print(display)

end_game=False
while not end_game:

    guess=input("guess the letter from list").lower()

    for position in range(len(chosen_word)):
            letter=chosen_word[position]
            if letter==guess:
                display[position]=letter
    print(display)  
    if "_" not in display:
     end_game=True
     print("win")    
    
    if guess not in chosen_word:
        lives-=1
        print(f"Wrong choose {chosen_word}")
        print(f"{lives} more lives left")
    else:
        print(f"Correct Choice\n {lives} more lives left")
         
    if lives==0:
        end_game=True
        print("You lose")
    print(stages[lives])      


   



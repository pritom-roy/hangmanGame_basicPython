import random
import art_work
import word_details

#for clearing the consol used replit ide
from replit import clear

print(art_work.logo)

word_list = word_details.word_list
guess_bar=[]
stages=art_work.stages
word=random.choice(word_list)
life=7

cont=False
for i in word:
  guess_bar.append("_")

print(art_work.man)
print("To save this man try to guess this word: ")
print(f"{' '.join(guess_bar)}")

while not cont:   
    a=input("\nGuess a letter: ").lower()
    clear()
    if a in guess_bar:
        print(f"\nYou have already guessed the letter '{a}'\nTry another\n")
        
    for i in range(len(word)):
        if word[i]==a:
            guess_bar[i]=a
        
    if not a in word:
        print(f"'{a}' is not in the word")
        life -= 1
        print(stages[life])
        if life == 0:
            cont = True
            print(stages[life])
            print("You lose.")
            
    print(f"{' '.join(guess_bar)}")
    if(life==0):
        print(f"The word was {word}")
    
    if "_" not in guess_bar:
        cont = True
        print("You win.")
        
    

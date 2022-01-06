#Guess the number Game

import random


def guess_number():
    number= random.randrange(60,200)
    player_name=input("Enter Your Name:")
    Confirm_play=input("Would you like to start the game?(Enter yes/no)")
    
    attempts=0
    
    while Confirm_play.lower()=="yes":
        
        guess=int(input("Guess any number between 60 and 200,"))
        
        if guess<60 or guess>200:
            print("Please guess any number in the Range.")
            
            
        elif guess == number:
            print("Congratulations!",player_name,'YOU WON !!')
            attempts+=1
            print("It took you",attempts,"attempts to win this Game.")
            break    
            
                
        elif guess > number:
            print("HINT: try smaller number")
            attempts+=1
            
        elif guess < number:
            print("HINT: try larger number")
            attempts+=1
                
        else:
            print("Thanks",player_name,"for your time.")
         
guess_number()
            
                

#!/usr/bin/env python
# coding: utf-8

# In[29]:


import random

player_score = 0
computer_score = 0
again = 1
print("Welcome to the rock paper scissors game..!!")
print("3 Points to win!")
print("1.) Rock  2.) Paper   3.) Scissors")
print("Chose any of the above action.")
while True:
    player_score = 0
    computer_score = 0
    while(player_score<3 and computer_score<3):
        computer_choice = random.randint(1,3)
        player_choice = int(input("Number: "))
        if(player_choice == computer_choice):
            player_score = player_score + 1
            computer_score = computer_score + 1
            print(player_score)
            print(computer_score)
        elif(player_choice == 1 and computer_choice == 2):
            computer_score = computer_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        elif(computer_choice == 1 and player_choice == 2):
            player_score == player_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        elif(player_choice == 2 and computer_choice == 3):
            computer_score = computer_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        elif(computer_choice == 2 and player_choice == 3):
            player_score = player_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        elif(player_choice == 1 and computer_choice == 3):
            player_score = player_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        elif(computer_choice == 1 and player_choice == 3):
            computer_score = computer_score + 1
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        else:
            print("Invalid Input...")
    else:
        if(player_score>computer_score):
            print("You won the game!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for playing!")
                break            
        elif(player_score==computer_score):
            print("It is a tie...")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for playing!")
                break        
        else:
            print("You loose!, try again?")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for playing!")
                print("Game ended")
                break


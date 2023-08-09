import tkinter as tk
from tkinter import messagebox
import random


def computer_check():
    choices = ['rock',"paper",'scissors']
    return random.choice(choices)

def whoWin(player,computer):
    if player == computer:
        return "Game is tie, no one wins!"
    elif(
        (player =='rock'and computer == 'scissor')
        or (player == 'paper' and computer=='rock')
        or (player =='scissors' and computer=='paper')
    ) :
        return 'hurry you win the game ....!'
    else:
            return 'you lose the game,computer wins the game'
               

def play_game(player):
     computer = computer_check()
     result = whoWin(player, computer)
     messagebox.showinfo("Result",f"your choice: {player}\n computer choice: {computer}\n {result}")

    
def window():
     app = tk.Tk()
     app.title("Rock Paper Scissors Game")
     app.geometry("300x300")

     

     choices = ['rock',"paper",'scissors']
     for i in choices:
          button = tk.Button(app,text=i,command=lambda insert=i:play_game(insert))
          button.pack(pady=20)
    
     app.mainloop()

if __name__ == "__main__":
     window()


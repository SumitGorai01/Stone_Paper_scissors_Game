from tkinter import *
from PIL import Image, ImageTk
from random import randint
root=Tk()
#root.geometry("1300x500")
root.minsize(1300,500)
root.title("Rock Paper Scissor")
root.configure(background="#c603fc")

rock_img=ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_image=ImageTk.PhotoImage(Image.open("scissors_user.png"))
rock_comp=ImageTk.PhotoImage(Image.open("rock_image.png"))
scissor_comp=ImageTk.PhotoImage(Image.open("scissors.png"))
paper_comp=ImageTk.PhotoImage(Image.open("paper-comp.png"))

#display image
user = Label(root,image=scissor_image,bg="#9b59b6")
computer = Label(root,image=scissor_comp,bg="#9b59b6")
computer.grid(row=1,column=0)
user.grid(row=1,column=4)

#score
playerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
playerScore.grid(row=1,column=3)
computerScore.grid(row=1,column=1)

# button
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white", command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

# name
user_name =Label(root,font=50 , text="USER", bg="#9b59b6", fg="white")
comp_name =Label(root,font=50 , text="COMPUTER", bg="#9b59b6", fg="white")
user_name.grid(row=0,column=3)
comp_name.grid(row=0,column=1)

#message
msg = Label(root,font=50, bg="#9b59b6",fg="white")
msg.grid(row=3, column=2)

#update choice

choices = ["rock","paper","scissor"]

def updateChoice(x):

    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice =="rock":
        computer.configure(image=rock_comp)
    elif compChoice == "paper":
        computer.configure(image=paper_comp)
    else:
        computer.configure(image=scissor_comp)

    #for user
    if x=="rock":
        user.configure(image=rock_img)
    elif x=="paper":
        user.configure(image=paper_img)
    else:
        user.configure(image=scissor_image)

    checkWin(x,compChoice)

# update message
def updateMessage(x):
    msg['text']=x

#update user score
def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

#update user score
def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

# check winner

def checkWin(player, computer):
    if player== computer:
        updateMessage("Match Tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Ohh!! You Loose This Match ...")
            updateCompScore()
        else:
            updateMessage("Hurry ! You won this match...")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Ohh! You loose this match...")
            updateCompScore()
        else:
            updateMessage("Hurry ! You won this match...")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Ohh! You loose this match...")
            updateCompScore()
        else:
            updateMessage("Hurry! You won this match...")
            updateUserScore()
    else:
        pass


root.mainloop()
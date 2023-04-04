from tkinter import *
import random

window = Tk()

window.geometry("800x400")
window.title("Rock Scissors Paper Lizard Spock")

frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(frame, text="Rock Scissors Paper Lizard Spock", font="100")
name.place(x=270, y=20)

label1 = Label(frame, text="Player", font="normal 15")

label2 = Label(frame, text="VS", font="normal 15")

label3 = Label(frame, text="Computer", font="normal 15")

label1.place(x=80, y=50, width=100)
label2.place(x=350, y=50, width=100)
label3.place(x=600, y=50, width=100)

rock_png = PhotoImage(file="rock.png")
scissors_png = PhotoImage(file="scissors.png")
paper_png = PhotoImage(file="paper.png")
lizard_png = PhotoImage(file="lizard.png")
spock_png = PhotoImage(file="spock.png")

user_image = Label(frame, image="")
user_image.place(x=70, y=100)

comp_image = Label(frame, image="")
comp_image.place(x=590, y=100)

lable4 = Label(frame, text="", font="normal 20", width = 15, borderwidth=2, relief="solid")
lable4.place(x=275, y=200)

def Rock():
    user = "Rock"
    computer = random.choice(["Rock", "Scissors", "Paper", "Lizard", "Spock"])
    user_image.config(image=rock_png)
    if user == computer:
        lable4.config(text="Tie")
        comp_image.config(image=rock_png)
    elif computer == "Paper":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=paper_png)
    elif computer == "Spock":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=spock_png)
    else:
        lable4.config(text="You Win!")
        comp_image.config(image=scissors_png)
        comp_image.config(image=lizard_png)

b1 = Button(frame, text="Rock", font="10", width=20, command=Rock)
b1.place(x=100, y=300)

def Scissors():
    user = "Scissors"
    computer = random.choice(["Rock", "Scissors", "Paper", "Lizard", "Spock"])
    user_image.config(image=scissors_png)
    if user == computer:
        lable4.config(text="Tie")
        comp_image.config(image=scissors_png)
    elif computer == "Rock":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=rock_png)
    elif computer == "Spock":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=spock_png)
    else:
        lable4.config(text="You Win!")
        comp_image.config(image=paper_png)
        comp_image.config(image=lizard_png)

b2 = Button(frame, text="Scissors", font="10", width=20, command=Scissors)
b2.place(x=300, y=300)

def Paper():
    user = "Paper"
    computer = random.choice(["Rock", "Scissors", "Paper", "Lizard", "Spock"])
    user_image.config(image=paper_png)
    if user == computer:
        lable4.config(text="Tie")
        comp_image.config(image=paper_png)
    elif computer == "Scissors":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=scissors_png)
    elif computer == "Lizard":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=lizard_png)
    else:
        lable4.config(text="You Win!")
        comp_image.config(image=rock_png)
        comp_image.config(image=spock_png)

b3 = Button(frame, text="Paper", font="10", width=20, command=Paper)
b3.place(x=500, y=300)

def Lizard():
    user = "Lizard"
    computer = random.choice(["Rock", "Scissors", "Paper", "Lizard", "Spock"])
    user_image.config(image=lizard_png)
    if user == computer:
        lable4.config(text="Tie")
        comp_image.config(image=lizard_png)
    elif computer == "Rock":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=rock_png)
    elif computer == "Lizard":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=lizard_png)
    else:
        lable4.config(text="You Win!")
        comp_image.config(image=paper_png)
        comp_image.config(image=spock_png)

b4 = Button(frame, text="Lizard", font="10", width=20, command=Lizard)
b4.place(x=190, y=340)

def Spock():
    user = "Spock"
    computer = random.choice(["Rock", "Scissors", "Paper", "Lizard", "Spock"])
    user_image.config(image=spock_png)
    if user == computer:
        lable4.config(text="Tie")
        comp_image.config(image=spock_png)
    elif computer == "Paper":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=paper_png)
    elif computer == "Lizard":
        lable4.config(text="Computer Wins!")
        comp_image.config(image=lizard_png)
    else:
        lable4.config(text="You Win!")
        comp_image.config(image=rock_png)
        comp_image.config(image=scissors_png)

b5 = Button(frame, text="Spock", font="10", width=20, command=Spock)
b5.place(x=390, y=340)

window.mainloop()
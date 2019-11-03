import random
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("600x400")
window.title("Rock Paper Scissors Game")

# declare integer
outcome = ""
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

# photo on button
rck = PhotoImage(file = "iconfinder_hand-rock-o_1608372.png")
rck = rck.subsample(5, 5) 
ppr = PhotoImage(file = "iconfinder_hand-stop-o_1608369.png")
ppr = ppr.subsample(5, 5)
scr = PhotoImage(file = "iconfinder_hand-peace-o_1608374.png")
scr = scr.subsample(5, 5)

# RPS FUNCTION 
def Rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def Paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def Scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)



#CONVERT TO NO.
def choice_to_number(choice):
    rps = {'Rock':0,'Paper':1,'Scissor':2}
    return rps[choice]

#COMPUTER CHOICE
def random_computer_choice():
    return random.choice(['Rock','Paper','Scissor'])

#REAULT FUNCTION
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    global outcome
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)

    if(user==comp):
        outcome="TIE"

    elif((user-comp)%3==1):
        outcome="YOU WIN !!"
        USER_SCORE+=1
    else:
        outcome="COMPUTER WINS ;("
        COMP_SCORE+=1

#DISPLAY TEXT-AREA
    text_area = tk.Text(master=window, height=10, width=30, font=("Helvetica", 25), bg="#FFFFFF")
    text_area.grid(row=1, columnspan=3, pady=(50,0))

    answer = " \n Your Choice: {uc} \n\n Computer's Choice : {cc} \n\n Your Score : {u} \n\n Computer Score: {c} \n\n {s} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE,s=outcome)
    text_area.insert(tk.END,answer)
    

# BUTTONS
button1 = tk.Button(master=window,text="       Rock       ",height=170,width=200,image=rck,compound="top",bg="skyblue",font = ("Times", 20),command=Rock)
button1.grid(column=0,row=0,padx=(70,100),pady=(10,50))

button2 = tk.Button(master=window,text="       Paper      ",height=170,width=200,image=ppr,compound="top",bg="pink",font = ("Times", 20),command=Paper)
button2.grid(column=1,row=0,padx=(0,100),pady=(10,50))

button3 = tk.Button(master=window,text="      Scissor     ",height=170,width=200,image=scr,compound="top",bg="lightgreen",font = ("Times", 20),command=Scissor)
button3.grid(column=2,row=0,padx=(0,100),pady=(10,50))

window.mainloop()
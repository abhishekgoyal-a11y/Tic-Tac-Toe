from tkinter import *
clicked = True
count = 0

def restart_game():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,turn
    global clicked,count
    clicked = True
    count = 0
    
    turn= Label(screen,text="Turn - X",height=2, font=("Times", "9", "bold italic"))
    turn.grid(row=0,column=0,columnspan=3)
    
    b1 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b1))
    b2 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b2))
    b3 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b3))
    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)

    b4 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b4))
    b5 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b5))
    b6 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b6))
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)

    b7 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b7))
    b8 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b8))
    b9 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b9))
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)


# WHEN GAME IS OVER OR DRAW, DISABLE THE BUTTON
def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# CHECKING THE WINNER
def check_winner():
    # CHECKING FOR X

    # CHECKING IN HORIZONTAL    
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        disable_button()
    if b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        print(b1["text"],"is winner")
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        disable_button()
    if b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        print(b1["text"],"is winner")
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        disable_button()

    # CHECKING IN VERTICAL    
    if b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        disable_button()
    if b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        print(b1["text"],"is winner")
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        disable_button()
    if b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        print(b1["text"],"is winner")
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        disable_button()
    

    # CHECKING IN DIAGONAL    
    if b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        disable_button()
    if b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        print(b1["text"],"is winner")
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        disable_button()
    
    # CHECKING FOR O

    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        disable_button()
    if b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        print(b1["text"],"is winner")
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        disable_button()
    if b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        print(b1["text"],"is winner")
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        disable_button()

    # CHECKING IN VERTICAL    
    if b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        disable_button()
    if b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        print(b1["text"],"is winner")
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        disable_button()
    if b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        print(b1["text"],"is winner")
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        disable_button()
    

    # CHECKING IN DIAGONAL    
    if b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        print(b1["text"],"is winner")
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        disable_button()
    if b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        print(b1["text"],"is winner")
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        disable_button()
        
# CHECK WHEN BUTTON
def b_click(value):
    global clicked , count,turn
    if value["text"]==" " and clicked== True:
        value["text"]="X"
        clicked = False
        count+=1
        check_winner()
        turn["text"]="Turn - O"
    elif value["text"]==" " and clicked== False:
        value["text"]="O"
        clicked = True
        count+=1
        check_winner()
        turn["text"]="Turn - X"
        
# SCREEN INITIALIZE
screen = Tk()
screen.title("Tic Tac Toe")
screen.minsize(240,320)
screen.maxsize(240,320)

turn= Label(screen,text="Turn - X",height=2, font=("Times", "9", "bold italic"))
turn.grid(row=0,column=0,columnspan=3)

# BUTTON DEFINE
b1 = Button(screen,text=" ", font=("Times", "9", "bold italic") ,height=5,width=10,command=lambda: b_click(b1))
b2 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b2))
b3 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b3))
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b4))
b5 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b5))
b6 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b6))
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b7))
b8 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b8))
b9 = Button(screen,text=" ", font=("Times", "9", "bold italic"),height=5,width=10,command=lambda: b_click(b9))
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

# RESTART BUTTON
restart_game = Button(screen,text="Restart Game",padx=81,command=restart_game)
restart_game.grid(row=4,column=0,columnspan=3)

screen.mainloop()

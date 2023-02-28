from tkinter import *


window = Tk()
window.iconbitmap("icon.ico")
window.title("Tic-Tac-Toe")
def button_check(row,column):
    if buttons[row][column]['text'] != "":
        print("Nice")

def check_winner(row,column):
    global main_Label
    global spaces
    global buttons
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "" :
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        main_Label.config(text=buttons[0][0]['text'] + " wins")
        spaces = 2

    elif buttons[0][2]['text'] == buttons[2][0]['text'] == buttons[1][1]['text'] != "" :
        buttons[0][2].config(bg="green")
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        main_Label.config(text=buttons[2][0]['text'] + " wins")
        spaces = 2
    

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            main_Label.config(text=buttons[row][0]['text'] + " wins")
            spaces = 2
        
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            main_Label.config(text=buttons[0][column]['text'] + " wins")
            spaces =2
    else:
        spaces -= 1
        if spaces == 0:
            main_Label.config(text="Tie!")
    
    


def click(row,column):
    button_check(row,column)
    global X
    if buttons[row][column]['text'] != "":
        print("Nice")
    else:
        global main_Label
        if X == True:
            main_Label.config(text="O's turn")
            buttons[row][column].config(text="X")
            check_winner(row,column)
            X = False
        else:
            main_Label.config(text="X's turn")

            buttons[row][column].config(text="O")
            check_winner(row,column)
            X = True
        
        


def restart():
    global spaces
    spaces = 9
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="white")
    main_Label.config(text="X's turn")
 

main_Label = Label(font=('consolas',40),text = "X's turn")
main_Label.pack(side="top")

restart_button = Button(font=('consolas',20),width=6,height=2,text='restart',command = restart)
restart_button.pack(side="top")

frame = Frame(window,)
frame.pack(side="top")

buttons = [[0,0,0],[0,0,0],[0,0,0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,font =('consolas',40),height=2,width=5,bg= "white",command= lambda row=row,column=column:click(row,column))

        buttons[row][column].grid(row = row,column = column)

X = True
spaces = 9

window.mainloop()
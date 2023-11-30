from tkinter import *
# from tkinter.ttk import *
from tkinter import messagebox


player_state = False
x_wins = 0
zero_wins = 0
draw = 0


def button_click_11():
    global player_state
    if not button_11["text"]:
        if player_state:
            button_11.config(text="0")
        else:
            button_11.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_12():
    global player_state
    if not button_12["text"]:
        if player_state:
            button_12.config(text="0")
        else:
            button_12.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_13():
    global player_state
    if not button_13["text"]:
        if player_state:
            button_13.config(text="0")
        else:
            button_13.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_21():
    global player_state
    if not button_21["text"]:
        if player_state:
            button_21.config(text="0")
        else:
            button_21.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_22():
    global player_state
    if not button_22["text"]:
        if player_state:
            button_22.config(text="0")
        else:
            button_22.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_23():
    global player_state
    if not button_23["text"]:
        if player_state:
            button_23.config(text="0")
        else:
            button_23.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_31():
    global player_state
    if not button_31["text"]:
        if player_state:
            button_31.config(text="0")
        else:
            button_31.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_32():
    global player_state
    if not button_32["text"]:
        if player_state:
            button_32.config(text="0")
        else:
            button_32.config(text="X")
        player_state = not player_state
    check_the_winner()


def button_click_33():
    global player_state
    if not button_33["text"]:
        if player_state:
            button_33.config(text="0")
        else:
            button_33.config(text="X")
        player_state = not player_state
    check_the_winner()


def create_game():
    normal_buttons()
    button_11.config(text="")
    button_12.config(text="")
    button_13.config(text="")
    button_21.config(text="")
    button_22.config(text="")
    button_23.config(text="")
    button_31.config(text="")
    button_32.config(text="")
    button_33.config(text="")


def check_the_winner():
    global x_wins, zero_wins, draw
    if button_11["text"] == "X" and button_21["text"] == "X" and button_31["text"] == "X" or\
            button_12["text"] == "X" and button_22["text"] == "X" and button_32["text"] == "X" or\
            button_13["text"] == "X" and button_23["text"] == "X" and button_33["text"] == "X" or\
            button_11["text"] == "X" and button_12["text"] == "X" and button_13["text"] == "X" or\
            button_21["text"] == "X" and button_22["text"] == "X" and button_23["text"] == "X" or\
            button_31["text"] == "X" and button_32["text"] == "X" and button_33["text"] == "X" or\
            button_11["text"] == "X" and button_22["text"] == "X" and button_33["text"] == "X" or\
            button_13["text"] == "X" and button_22["text"] == "X" and button_31["text"] == "X":
        # print("X - won!")
        disable_buttons()
        x_wins += 1
        messagebox.showinfo('Win', 'X - won!')
    elif button_11["text"] == "0" and button_21["text"] == "0" and button_31["text"] == "0" or\
            button_12["text"] == "0" and button_22["text"] == "0" and button_32["text"] == "0" or\
            button_13["text"] == "0" and button_23["text"] == "0" and button_33["text"] == "0" or\
            button_11["text"] == "0" and button_12["text"] == "0" and button_13["text"] == "0" or\
            button_21["text"] == "0" and button_22["text"] == "0" and button_23["text"] == "0" or\
            button_31["text"] == "0" and button_32["text"] == "0" and button_33["text"] == "0" or\
            button_11["text"] == "0" and button_22["text"] == "0" and button_33["text"] == "0" or\
            button_13["text"] == "0" and button_22["text"] == "0" and button_31["text"] == "0":
        print("0 - won!")
        disable_buttons()
        zero_wins += 1
        messagebox.showinfo('Win', '0 - won!')
        # label.config(text=f'X wins-{x_wins}, 0 wins-{zero_wins}, draw-{draw}')
    elif button_11["text"] and button_12["text"] and button_13["text"]\
            and button_21["text"] and button_22["text"] and button_23["text"]\
            and button_31["text"] and button_32["text"] and button_33["text"]:
        print("")
        draw += 1
        disable_buttons()
        messagebox.showinfo('Win', 'draw')
    label.config(text=f'X wins-{x_wins}, 0 wins-{zero_wins}, draw-{draw}')


def disable_buttons():
    button_11['state'] = 'disable'
    button_12['state'] = 'disable'
    button_13['state'] = 'disable'
    button_21['state'] = 'disable'
    button_22['state'] = 'disable'
    button_23['state'] = 'disable'
    button_31['state'] = 'disable'
    button_32['state'] = 'disable'
    button_33['state'] = 'disable'


def normal_buttons():
    button_11['state'] = 'normal'
    button_12['state'] = 'normal'
    button_13['state'] = 'normal'
    button_21['state'] = 'normal'
    button_22['state'] = 'normal'
    button_23['state'] = 'normal'
    button_31['state'] = 'normal'
    button_32['state'] = 'normal'
    button_33['state'] = 'normal'


root = Tk()

root.title("Tic-tac-toe v.10")

button_11 = Button(command=button_click_11)
button_11.grid(column=1, row=1, ipadx=40, ipady=60)
button_12 = Button(command=button_click_12)
button_12.grid(column=1, row=2, ipadx=40, ipady=60)
button_13 = Button(command=button_click_13)
button_13.grid(column=1, row=3, ipadx=40, ipady=60)

button_21 = Button(command=button_click_21)
button_21.grid(column=2, row=1, ipadx=40, ipady=60)
button_22 = Button(command=button_click_22)
button_22.grid(column=2, row=2, ipadx=40, ipady=60)
button_23 = Button(command=button_click_23)
button_23.grid(column=2, row=3, ipadx=40, ipady=60)

button_31 = Button(command=button_click_31)
button_31.grid(column=3, row=1, ipadx=40, ipady=60)
button_32 = Button(command=button_click_32)
button_32.grid(column=3, row=2, ipadx=40, ipady=60)
button_33 = Button(command=button_click_33)
button_33.grid(column=3, row=3, ipadx=40, ipady=60)

Button(text="NEW GAME", command=create_game).grid(column=1, row=4, columnspan=3, sticky=NSEW)
label = Label(text="X wins-0, 0 wins-0, draw-0 ")
label.grid(column=1, row=5, columnspan=3)


root.mainloop()

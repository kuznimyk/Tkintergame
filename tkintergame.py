"""
Session: 1D01
Group Members: Mykyta Kuznietsov, Mark Hanson,
Due Date: October 6, 2023
Assignment 1: Python Introduction Using Turtle Summary:
Summary of what the program does
Resources Used : [optional, only if you have global resources]
https://docs.python.org/3/library/turtle.html
"""
import tkinter
import tkinter.messagebox
from random import *
from tkinter import *
from tkinter import ttk
#create the window
window  = Tk()
window.title("Welcome")
window.geometry("610x1200")

#variables for the number of turns
redturn = 0
blackturn = 0

#variable to track the turn
turn = 'red'



#dictionary to store the buttons (row and column and the keys and the button itself is a value)
dict = {}

'''variables to track the score of black and red players, score itself is the frist element of the list
lists are used because they are pointers and their values can be directly changed though another vatiable'''
score1 = [0]
score2 = [0]

"""Mark Hanson-Torwalt's Part start"""
def turnoff():# turn off the ablity to click buttons
    for i in range(9):
        for j in range(9):
            dict[(i,j)].configure(state = DISABLED)



def turnon(): #turn on the ablity to click the buttons
    for i in range(9):
        for j in range(9):
            if dict[(i, j)].cget('bg') == 'red':
                dict[(i, j)].configure(state=NORMAL)



#variables to track how many turns black and red players have
def NumOfTurnsWindow(): #creating a new window with an input bar for number of moves each player has
    global newWindow
    global entryNumber
    turnoff()
    newWindow = Toplevel(window)
    newWindow.geometry("200x200")
    newWindow.title("How many turns do you wish to have?")
    # button will start the game once a move count has been chosen.
    # window will close.
    startButton =Button(newWindow, text="Click to start game", command=lambda: CloseNewWindow())
    startButton.pack()
    name = Label(newWindow, text="Number of turns you want", width=20)
    name.pack()
    # creating an entry bar for players to add number of turns.
    entryNumber = Entry(newWindow, width=50)
    entryNumber.pack()
    entryNumber.insert(0, " ")



# creating a def to close the window after number of turns has been picked
def CloseNewWindow():
    print(entryNumber.get())
    global blackturn
    global redturn
    # using .get to use the number the player has input into the game
    blackturn = int(entryNumber.get())
    redturn = int(entryNumber.get())
    turnon()
    newWindow.destroy()












#function to paint the background color of the button
def paintcolor():
    num = randint(0,1)
    if num == 1:
        return "red"
    else:return "black"


#fucntion that deactivates the buttons after each turn
def deactivatebuttons(color):
    for i in range(9):
        for j in range(9):
            #deactivate all the buttons if black
            if blackturn != 0:
                if dict[(i, j)].cget('bg') == color:
                    dict[(i, j)].configure(state=DISABLED)
                else:
                    dict[(i, j)].configure(state=NORMAL)
            else:
                if dict[(i, j)].cget('bg') == color:
                    dict[(i, j)].configure(state=DISABLED)
                else:
                    dict[(i, j)].configure(state=DISABLED)
"""Mark Hanson-Torwalt's end"""


'''
Mykyta Kuznietsov's part start

'''


#function that paints the buttons above the pressed button
def painttop(color,  button, nextbut,x,y):
    #
    score = []
    #determine which score we will increase
    if color == 'black':
        score = score2
    else:
        score = score1
    #set the counter
    counter  = -1
    paint = True
    #go through the buttons above the pressed ones until the players color is reached or until the border is reached
    while nextbut.cget('bg') != color:
        counter += 1
        #if the nextbut reaches the boundary, then the top buttons will not be painted
        if x - counter == -1:
            paint = False
            break;
        #move to the upper button
        nextbut = dict[(x - counter, y)]
    if paint == True:
        #paint the buttons above
        for i in range(counter):
            dict[(x - i, y)].configure(bg=color)
        score[0] += counter
        counter = -1
    else:
        #if the nextbut reached the boundary, then don't paint anything and reset the counter
        button.configure(bg=color)
        counter = -1
        paint = True
    return

def paintbot(color, button, nextbut,x,y):
    score = []
    if color == 'black':
        score = score2
    else:
        score = score1
    counter  = -1
    paint = True
    if color == color:
        nextbut.configure(bg='white')
    else:
        nextbut.configure(bg = color)
    #go through the buttons below the pressed ones until the players color is reached or until the border is reached
    while nextbut.cget('bg') != color:
        #if the nextbut reaches the boundary, then the bottom buttons will not be painted
        counter += 1
        if 9 - counter == x:
            paint = False
            break;
            # move to the upper button
        nextbut = dict[(x + counter, y)]
    if paint == True:
        #paint the buttons below
        for i in range(counter):
            dict[(x + i, y)].configure(bg=color)
        score[0] += counter - 1
        counter = -1
    else:
        #if the nextbut reached the boundary, then don't paint anything and reset the counter
        button.configure(bg=color)
        counter = -1
        paint = True

def paintright(color,button, nextbut,x,y):
    score = []
    if color == 'black':
        score = score2
    else:
        score = score1
    counter  = -1
    paint = True
    if color == color:
        nextbut.configure(bg='white')
    else:
        nextbut.configure(bg = color)
    # go through the buttons on the right until the player colour is reached or until boarder in reached
    while nextbut.cget('bg') != color:
        # if the nextbut reaches the boundary, then the left side buttons will not be painted

        counter += 1
        if 9 - counter == y:
            paint = False
            break;
        # move to the upper button
        nextbut = dict[(x, y + counter)]
    if paint == True:
        #paint the buttons above

        for i in range(counter):
            dict[(x, y + i)].configure(bg=color)
        score[0] += counter - 1
        counter = -1
    else:
        #if the nextbut reached the boundary, then don't paint anything and reset the counter

        button.configure(bg=color)
        counter = -1
        paint = True
    return

def paintleft(color, button, nextbut,x,y):
    score = []
    if color == 'black':
        score = score2
    else:
        score = score1
    counter  = -1
    paint = True
    if color == color:
        nextbut.configure(bg='white')
    else:
        nextbut.configure(bg = color)
    # go through the buttons on the left until the player colour is reached or until boarder in reached
    while nextbut.cget('bg') != color:
        counter += 1
        if y - counter == -1:
            paint = False
            break;
        nextbut = dict[(x, y - counter)]
    if paint == True:
        for i in range(counter):
            dict[(x, y - i)].configure(bg=color)
        score[0] += counter - 1
        counter = -1
    else:
        button.configure(bg=color)
        counter = -1
        paint = True
    return



def changecolor( x, y):
    global redturn
    global blackturn
    global score1
    global score2
    #place row and column values in a tuple
    cord = (x,y)
    #take out the button variable from the dictionary using row and column values
    but = dict[cord]
    #get the background color or the pressed button

    color = but.cget('bg')
    #anotehr pointer to the current button
    nextbut = but
    #counter variable to count the ammount of boxes that should be painted
    counter = -1
    #variable that allows to paint certain buttons
    paint = True
    #variables to relocate: color to paint, nextbut, x-cord,y-cord
    if color == 'red':
        #paint buttons on top
        painttop('black', but,nextbut,x,y)
        #paint buttons on the bottom
        nextbut = but
        paintbot('black', but,nextbut,x,y)
        #paint buttons on the right
        nextbut = but
        paintright('black', but,nextbut,x,y)
        #paint buttons on the left
        nextbut = but
        paintleft('black', but,nextbut,x,y)
        deactivatebuttons('red')

        redturn  = redturn - 1
        turn = 'black'
        colorOfPlayerTurn.configure(bg = 'red')
        playButtonColor.configure(bg=  'black')
        numberOfTurns.configure(text= str(blackturn))
        playerBlackScore.configure(text = str(score2[0]))

    else:
        painttop('red', but, nextbut, x, y)
        # paint buttons on the bottom
        nextbut = but
        paintbot('red', but, nextbut, x, y)
        # paint buttons on the right
        nextbut = but
        paintright('red', but, nextbut, x, y)
        # paint buttons on the left
        nextbut = but
        paintleft('red', but, nextbut, x, y)
        deactivatebuttons("black")
        blackturn = blackturn - 1
        turn  = 'red'

        #change the label responsible for showing the score
        playerRedScore.configure(text= str(score1[0]))
        #change the color of the buttons accordingly
        colorOfPlayerTurn.configure(bg = 'black')
        playButtonColor.configure(bg=  'red')
        #change the number of turns for the player
        numberOfTurns.configure(text= str(redturn))
        #if players run out of truns, then pop the messagebox showing which player won, depending on the score
        if blackturn ==0  and redturn == 0:
            print(blackturn)
            if score1[0] < score2[0]:
                tkinter.messagebox.showinfo("Winner", "Player2")
            elif score1[0] == score2[0]:
                tkinter.messagebox.showinfo("Winner", "DRAW")
            else:
                tkinter.messagebox.showinfo("Winner", "Player1")


# menu that shows the ammount of turns and what player's turn it's right now

'''
Mykyta Kuznietsov's part end'''
'''Mark Hanson-Torwalt's part start'''
def gameLogistics():
    global numberOfTurns
    global playerBlackScore
    global colorOfPlayerTurn
    global playButtonColor
    global playerRedScore

# creating the bottom section of the game board to identify different game statistics.

    # Stating how many turns the player has left 1
    frameOne = Frame(master = window, width = 8, height =4)
    frameOne.grid(row = 9, column = 0)
    remainingTurns = Label(master = frameOne, text="  Turn  \n  number")
    remainingTurns.pack()

    # Number of turns that each player has 2
    frameTwo = Frame(master = window, width = 8, height = 4)
    frameTwo.grid(row = 10, column = 0)
    numberOfTurns = Label(master = frameTwo, text = str(blackturn))
    numberOfTurns.pack()

    # stating which players turn it is 3
    frameThree = Frame(master = window, width = 8, height = 4)
    frameThree.grid(row = 9, column = 2)
    changingPlayerTurn = Label(master = frameThree, text = 'It''s your \n turn:')
    changingPlayerTurn.pack()

    # colour of the players turn 4
    frameFour = Frame(master = window, width = 8, height= 4)
    frameFour.grid(row= 10, column = 2)
    colorOfPlayerTurn = Button(master = frameFour,bg = 'black', width = 8, height = 4, state = DISABLED)
    colorOfPlayerTurn.pack()

    # telling the player what colour they must click 5
    frameFive = Frame(master = window, width = 8, height = 4)
    frameFive.grid(column = 4, row = 9)
    colorToClick = Label(master = frameFive,text= 'Click on:')
    colorToClick.pack()

    # colour that the player must select to play game 6
    frameSix = Frame(master = window, width = 8, height = 4)
    frameSix.grid(row = 10, column = 4)
    playButtonColor = Button(master = frameSix, bg= 'red', height = 4, width = 8, state = DISABLED)
    playButtonColor.pack()

    # Stating player Red's score 7
    frameSeven = Frame(master = window, width = 8, height= 4)
    frameSeven.grid(column = 6, row = 9)
    redPlayer = Label(master = frameSeven, text = "Red\nscore")
    redPlayer.pack()

    # Showing what score player Red has 8
    frameEight = Frame(master = window, height = 4, width = 8)
    frameEight.grid(row = 10, column = 6)
    playerRedScore = Label(master = frameEight, text = str(0))
    playerRedScore.pack()

    # Stating player Black's score 9
    frameNine = Frame(master = window, width = 8, height= 4)
    frameNine.grid(column = 8, row = 9)
    blackPlayer = Label(master = frameNine, text = "Black\nscore")
    blackPlayer.pack()
    # Showing what player Black's score is 10

    frameTen = Frame(master = window, height = 4, width = 8)
    frameTen.grid(row = 10, column = 8)
    playerBlackScore = Label(master = frameTen, text = str(0))
    playerBlackScore.pack()
"""Mark Hanson-Torwalt's part End"""

#main code starts here

'''
Fucntion to create the buttons for the game, paint them and assign a command
'''

'''Mykyta Kuznietsov's part start'''
def createbuttons():
    for i in range(9):
        for j in range(9):
            #create a frame where the button will be located
            frame = Frame(master = window,relief = RAISED, borderwidth=1)
            #assign fram a grid
            frame.grid(row = i, column = j)
            #create the button and paint it into random color(black or red)
            button = Button(master = frame, height=4, width=8,  bg = paintcolor())
            #if the button is black, then disable it
            if button.cget('bg') == 'black':
                button.configure(state = DISABLED)
            #assign a comman to a button though the lambda funtion x and y will be the cordinates of the button
            button.configure(command = lambda  x = i, y = j: changecolor( x,y))
            button.pack()
            #make a dictionary with key - value where the key will be the tuple with cordinates of the button and
            dict[(i,j)] = button
'''
Mykyta Kuznietsov's part end
'''


createbuttons()
NumOfTurnsWindow()
gameLogistics()
window.mainloop()


"""
citations used
eclass forms created by Thibaud Lutellier 

for the lambda functions: 
https://realpython.com/python-lambda/

for specific tkinter variables:
https://docs.python.org/3/library/tkinter.html

for placing buttons inside the frame and fram inside the grid: 
https://python-course.eu/tkinter/buttons-in-tkinter.php

working and using the dictionary: 
https://realpython.com/python-dicts/

"""














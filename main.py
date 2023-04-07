from tkinter import *
from time import sleep

main = Tk()
main.title("Test")
main.configure(bg="white")
# main.geometry("500x500+900+200")#Vertical Size, Horizontal Size + X position when loaded+ Y position when loaded
main.resizable(0,0)



class Game:
    def __init__(self):
        # all the buttons
        self.b = [ #used for the buttons
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.states = [ #used to check for win
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
        self.current_player = "X"
        self.game_over = False
        self.count = 0
    def clicked(self,r,c):
        #this changes the states array
        self.states[r][c] = self.current_player 

        #this changes the labels on each of the buttons
        self.b[r][c].config(text = self.current_player)

        #DISABLES THE SELECTED BUTTON
        self.b[r][c]["state"] = DISABLED

        #SWITCHES BETWEEN 'O' and 'X'
        self.change_player()

        self.count += 1
        #AFTER EVERY TURN CHECK FOR THE WIN CONDITION
        self.check_for_win()


    def change_player(self):
        #changes the current player
        if(self.current_player == "O"):
            self.current_player = "X"
        else:
            self.current_player = "O"
    def makeBoard(self):
        for i in range(3):
            for j in range(3):                            
                self.b[i][j] = Button(
                                height = 4, width = 8,
                                font = ("Helvetica","20"),
                                fg = "black",
                                command = lambda r = i, c = j : self.clicked(r,c))
                self.b[i][j].grid(row = i, column = j, padx = 1 , pady = 1)
    def clear_board(self):
        #RESETS THE GAME TO BE ABLE TO CONTINUE
        count = 0
        for i in range(3):
            for j in range(3):
                # self.b[i][j].config(text = "")
                self.b[i][j] = 0
                self.states[i][j] = count
                count += 1
                
        self.game_over = False
        self.current_player = "X"
        self.makeBoard()
    def open_win_menu(self, winner):

        self.disable_buttons()
        newWindow = Toplevel(main)
 
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
    
        # sets the geometry of toplevel
        newWindow.geometry("200x200")
    
        # A Label widget to show in toplevel
        if(winner == "Tie"):
            Label(newWindow,text = winner).pack()
        else:
            Label(newWindow,text = winner + " is the winner").pack()

        Button(newWindow, text="New Game", command=lambda: [newWindow.destroy(), self.clear_board()]).pack()
    def check_for_win(self):
        #CHECKS FOR THE WIN AND CALLS THE FUNCTION TO DISPLAY THE WINNER
        #HORIZONTAL
        for i in range(3):
            if(self.states[i][0] == self.states[i][1] and self.states[i][0] == self.states[i][2]):
                self.game_over = True
                self.open_win_menu(self.states[i][0])
        #VERTICAl
        for i in range(3):
            if(self.states[0][i] == self.states[1][i] and self.states[0][i] == self.states[2][i]):
                self.game_over = True
                self.open_win_menu(self.states[0][i])
        #DIAGONAL
        if(self.states[0][0] == self.states[1][1] and self.states[0][0] == self.states[2][2]):
            self.game_over = True
            self.open_win_menu(self.states[0][0])
        if(self.states[0][2] == self.states[1][1] and self.states[0][2] == self.states[2][0]):
            self.game_over = True
            self.open_win_menu(self.states[0][2])
        #CHECKS FOR TIE
        if(self.count == 9 and self.game_over != True):
            self.game_over = True
            self.open_win_menu("Tie")
    def disable_buttons(self):
        #MAKES IT SO THAT EVERY BUTTON IS DISABLED
        for i in range(3):
            for j in range(3): 
                self.b[i][j]["state"] = DISABLED
                                                                                    




test = Game()
test.makeBoard()

main.mainloop()




# your code goes here
import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

R1 = []
R2 = []
R3 = []
C1 = []
C2 = []
C3 = []
D1 = []
D2 = []

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'

###########################


#=======================================================================================

#This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

#=======================================================================================

#This Function Checks position is empty or not
def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

#=======================================================================================

#This Function Checks player has won or not
def CheckWin():
    global Game
    #Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    #Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=Win
    #Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=Win
    #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game=Running

#======================================================================================================

#This function checks if player has played a valid move or not
def isValid(cell,restrictedPos):
    if (cell==restrictedPos):
        return False
    else:
        return True

#======================================================================================================

def defend(restrictX):
   
    #If the computer can't win in two moves, this function, when called, will make sure that the player does not get a chance to force a win in 2.
    #This is the fourth and the last step in our hierarchy.
    advanCells=[]
    if(restrictX==1):
        advanCells=[['2','3'],['4','7'],['5','9']]
        if(board[int(advanCells[0][0])]==' ' and board[int(advanCells[0][1])]=='O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])]=='O' and board[int(advanCells[0][1])]==' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])]==' ' and board[int(advanCells[1][1])]=='O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])]=='O' and board[int(advanCells[1][1])]==' '):
            return True, int(advanCells[1][1])
        elif (board[int(advanCells[2][0])]==' ' and board[int(advanCells[2][1])]=='O'):
            return True, int(advanCells[2][0])
        elif (board[int(advanCells[2][0])]=='O' and board[int(advanCells[2][1])]==' '):
            return True, int(advanCells[2][1])
        else:
            return False,None

    elif (restrictX==2):
        advanCells=[['1','3'],['5','8']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        else:
            return False,None


    elif (restrictX == 3):
        advanCells = [['1', '2'], ['6', '9'], ['5', '7']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        elif (board[int(advanCells[2][0])] == ' ' and board[int(advanCells[2][1])] == 'O'):
            return True, int(advanCells[2][0])
        elif (board[int(advanCells[2][0])] == 'O' and board[int(advanCells[2][1])] == ' '):
            return True, int(advanCells[2][1])
        else:
            return False, None

    elif (restrictX==4):
        advanCells=[['1','7'],['5','6']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        else:
            return False,None


    elif (restrictX==6):
        advanCells=[['3','9'],['4','5']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        else:
            return False,None

    elif (restrictX == 7):
        advanCells = [['1', '4'], ['8', '9'], ['5', '3']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        elif (board[int(advanCells[2][0])] == ' ' and board[int(advanCells[2][1])] == 'O'):
            return True, int(advanCells[2][0])
        elif (board[int(advanCells[2][0])] == 'O' and board[int(advanCells[2][1])] == ' '):
            return True, int(advanCells[2][1])
        else:
            return False,None

    elif (restrictX==8):
        advanCells=[['2','5'],['7','9']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        else:
            return False,None

    elif (restrictX == 9):
        advanCells = [['3', '6'], ['7', '8'], ['1', '5']]
        if (board[int(advanCells[0][0])] == ' ' and board[int(advanCells[0][1])] == 'O'):
            return True, int(advanCells[0][0])
        elif (board[int(advanCells[0][0])] == 'O' and board[int(advanCells[0][1])] == ' '):
            return True, int(advanCells[0][1])
        elif (board[int(advanCells[1][0])] == ' ' and board[int(advanCells[1][1])] == 'O'):
            return True, int(advanCells[1][0])
        elif (board[int(advanCells[1][0])] == 'O' and board[int(advanCells[1][1])] == ' '):
            return True, int(advanCells[1][1])
        elif (board[int(advanCells[2][0])] == ' ' and board[int(advanCells[2][1])] == 'O'):
            return True, int(advanCells[2][0])
        elif (board[int(advanCells[2][0])] == 'O' and board[int(advanCells[2][1])] == ' '):
            return True, int(advanCells[2][1])
        else:
            return False,None

#========================================================================================================

#This function will check if the computer can win by filling a row/column/diagonal containing the cell restricted for O, and returns the choice accordingly

def attack(Or,Xr):

    if ((Or == 1) or (Or == 2) or (Or == 3)):
        if (R1.count("X") == 1 and "O" not in R1  and " " in R1):
            if (R1[0] == " " and Or != 1):
                return True, 1
            if (R1[1] == " " and Or != 2):
                return True, 2
            if (R1[2] == " " and Or != 3):
                #print("I''m returning 3 ")
                return True, 3

    if (Or == 4 or Or == 5 or Or == 6):
        if (R2.count("X") == 1 and R2.count("O") == 0 and (" " in R2)):
            if (R2[0] == " " and Or != 4):

                return True, 4
            if (R1[1] == " " and Or != 5):
                return True, 5
            if (R1[2] == " " and Or != 6):
                return True, 6

    if (Or == 7 or Or == 8 or Or == 9):
        if (R3.count("X") == 1 and R3.count("O") == 0 and (" " in R3)):
            if (R3[0] == " " and Or != 7):
                return True, 7
            if (R3[1] == " " and Or != 8):
                return True, 8
            if (R3[2] == " " and Or != 9):
                return True, 9

    if (Or == 1 or Or == 4 or Or == 7):
        if (C1.count("X") == 1 and C1.count("O") == 0 and (" " in C1)):
            if (C1[0] == " " and Or != 1):
                return True, 1
            if (C1[1] == " " and Or != 4):
                return True, 4
            if (C1[2] == " " and Or != 7):
                return True, 7

    if (Or == 2 or Or == 5 or Or == 8):
        if (C2.count("X") == 1 and C2.count("O") == 0 and (" " in C2)):
            if (C2[0] == " " and Or != 2):
                return True, 2
            if (C2[1] == " " and Or != 5):
                return True, 5
            if (C2[2] == " " and Or != 8):
                return True, 8

    if (Or == 3 or Or == 6 or Or == 9):
        if (C3.count("X") == 1 and C3.count("O") == 0 and (" " in C3)):
            if (C3[0] == " " and Or != 3):
                return True, 3
            if (C3[1] == " " and Or != 6):
                return True, 6
            if (C3[2] == " " and Or != 9):
                return True, 9

    if (Or == 1 or Or == 5 or Or == 9):
        if (D1.count("X") == 1 and D1.count("O") == 0 and (" " in D1)):
            if (D1[0] == " " and Or != 1):
                return True, 1
            if (D1[1] == " " and Or != 5):
                return True, 5
            if (D1[2] == " " and Or != 9):
                return True, 9

    if (Or == 3 or Or == 5 or Or == 7):
        if (D2.count("X") == 1 and D2.count("O") == 0 and (" " in D2)):
            if (D2[0] == " " and Or != 3):
                return True, 3
            if (D2[1] == " " and Or != 5):
                return True, 5
            if (D2[2] == " " and Or != 7):
                return True, 7

    return False, None

#==============================================================================================

# defines global variables for storing the present state of rows, columns, and diagonals

def splitBoard():
    global R1,R2,R3,C1,C2,C3,D1,D2
    R1 = [board[1],board[2],board[3]]
    R2 = [board[4],board[5],board[6]]
    R3 = [board[7],board[8],board[9]]

    C1 = [board[1], board[4], board[7]]
    C2 = [board[2], board[5], board[8]]
    C3 = [board[3], board[6], board[9]]

    D1 = [board[1], board[5], board[9]]
    D2 = [board[3], board[5], board[7]]

#==============================================================================================

# this function checks if the computer has won

def CheckWinIn1(restrictX):
    # Horizontal winning condition Row1
    if (board[1] == board[2] and board[2] == 'X' and board[3] == ' ' and restrictX != 3):
        return 3
    elif (board[1] == board[3] and board[3] == 'X' and board[2] == ' ' and restrictX != 2):
        return 2
    elif (board[2] == board[3] and board[3] == 'X' and board[1] == ' ' and restrictX != 1):
        return 1
    # Horizontal winning condition Row2
    elif (board[4] == board[5] and board[5] == 'X' and board[6] == ' ' and restrictX != 6):
        return 6
    elif (board[4] == board[6] and board[6] == 'X' and board[5] == ' ' and restrictX != 5):
        return 5
    elif (board[5] == board[6] and board[6] == 'X' and board[4] == ' ' and restrictX != 4):
        return 4

    # Horizontal winning condition Row3
    elif (board[7] == board[8] and board[8] == 'X' and board[9] == ' ' and restrictX != 9):
        return 9
    elif (board[7] == board[9] and board[9] == 'X' and board[8] == ' ' and restrictX != 8):
        return 8
    elif (board[8] == board[9] and board[9] == 'X' and board[7] == ' ' and restrictX != 7):
        return 7

    # Vertical winning condition Col1
    elif (board[1] == board[4] and board[4] == 'X' and board[7] == ' ' and restrictX != 7):
        return 7
    elif (board[1] == board[7] and board[7] == 'X' and board[4] == ' ' and restrictX != 4):
        return 4
    elif (board[4] == board[7] and board[7] == 'X' and board[1] == ' ' and restrictX != 1):
        return 1

    # Vertical winning condition Col2
    elif (board[2] == board[5] and board[5] == 'X' and board[8] == ' ' and restrictX != 8):
        return 8
    elif (board[2] == board[8] and board[8] == 'X' and board[5] == ' ' and restrictX != 5):
        return 5
    elif (board[5] == board[8] and board[8] == 'X' and board[2] == ' ' and restrictX != 2):
        return 2

    # Vertical winning condition Col3
    elif (board[3] == board[6] and board[6] == 'X' and board[9] == ' ' and restrictX != 9):
        return 9
    elif (board[3] == board[9] and board[9] == 'X' and board[6] == ' ' and restrictX != 6):
        return 6
    elif (board[6] == board[9] and board[9] == 'X' and board[3] == ' ' and restrictX != 3):
        return 3

            # Leading Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == 'X' and board[9] == ' ' and restrictX != 9):
        return 9
    elif (board[1] == board[9] and board[9] == 'X' and board[5] == ' ' and restrictX != 5):
        return 5
    elif (board[5] == board[9] and board[9] == 'X' and board[1] == ' ' and restrictX != 1):
        return 1

     # Other Diagonal Winning Condition
    elif (board[3] == board[5] and board[5] == 'X' and board[7] == ' ' and restrictX != 7):
        return 7
    elif (board[3] == board[7] and board[7] == 'X' and board[5] == ' ' and restrictX != 5):
        return 5
    elif (board[5] == board[7] and board[7] == 'X' and board[3] == ' ' and restrictX != 3):
        return 3
    return None


#==================================================================================================

# this function prevents immediate loss of the computer by preventing the player from filling a row/column/diagonal in the next move

def AvoidLossIn1(restrictX, restrictO):
    # Horizontal winning condition Row1
    if (board[1] == board[2] and board[2] == 'O' and board[3] == ' ' and restrictX != 3 and restrictO !=3):
        return 3
    elif (board[1] == board[3] and board[3] == 'O' and board[2] == ' ' and restrictX != 2 and restrictO != 2):
        return 2
    elif (board[2] == board[3] and board[3] == 'O' and board[1] == ' ' and restrictX != 1 and restrictO != 1):
        return 1
    # Horizontal winning condition Row2
    elif (board[4] == board[5] and board[5] == 'O' and board[6] == ' ' and restrictO != 6 and restrictX!= 6 ):
        return 6
    elif (board[4] == board[6] and board[6] == 'O' and board[5] == ' ' and restrictO != 5 and restrictX != 5 ):
        return 5
    elif (board[5] == board[6] and board[6] == 'O' and board[4] == ' ' and restrictO != 4 and restrictX != 4):
        return 4

    # Horizontal winning condition Row3
    elif (board[7] == board[8] and board[8] == 'O' and board[9] == ' ' and restrictO != 9 and restrictX != 9):
        return 9
    elif (board[7] == board[9] and board[9] == 'O' and board[8] == ' ' and restrictO != 8 and restrictX != 8):
        return 8
    elif (board[8] == board[9] and board[9] == 'O' and board[7] == ' ' and restrictO != 7 and restrictX != 7):
        return 7

    # Vertical winning condition Col1
    elif (board[1] == board[4] and board[4] == 'O' and board[7] == ' ' and restrictO != 7 and restrictX != 7):
        return 7
    elif (board[1] == board[7] and board[7] == 'O' and board[4] == ' ' and restrictO != 4 and restrictX != 4):
        return 4
    elif (board[4] == board[7] and board[7] == 'O' and board[1] == ' ' and restrictO != 1 and restrictX != 1):
        return 1

    # Vertical winning condition Col2
    elif (board[2] == board[5] and board[5] == 'O' and board[8] == ' ' and restrictO != 8 and restrictX != 8):
        return 8
    elif (board[2] == board[8] and board[8] == 'O' and board[5] == ' ' and restrictO != 5 and restrictX != 5):
        return 5
    elif (board[5] == board[8] and board[8] == 'O' and board[2] == ' ' and restrictO != 2 and restrictX != 2):
        return 2

    # Vertical winning condition Col3
    elif (board[3] == board[6] and board[6] == 'O' and board[9] == ' ' and restrictO != 9 and restrictX != 9):
        return 9
    elif (board[3] == board[9] and board[9] == 'O' and board[6] == ' ' and restrictO != 6 and restrictX != 6):
        return 6
    elif (board[6] == board[9] and board[9] == 'O' and board[3] == ' ' and restrictO != 3 and restrictX != 3):
        return 3

        # Leading Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == 'O' and board[9] == ' ' and restrictO != 9 and restrictX != 9):
        return 9
    elif (board[1] == board[9] and board[9] == 'O' and board[5] == ' ' and restrictO != 5 and restrictX != 5):
        return 5
    elif (board[5] == board[9] and board[9] == 'O' and board[1] == ' ' and restrictO != 1 and restrictX != 1):
        return 1

        # Other Diagonal Winning Condition
    elif (board[3] == board[5] and board[5] == 'O' and board[7] == ' ' and restrictO != 7 and restrictX != 7):
        return 7
    elif (board[3] == board[7] and board[7] == 'O' and board[5] == ' ' and restrictO != 5 and restrictX != 5):
        return 5
    elif (board[5] == board[7] and board[7] == 'O' and board[3] == ' ' and restrictO != 3 and restrictX != 3):
        return 3
    return None


#==================================================================================================

# simulates the game for the player deciding the restriction first and the computer playing first

def simulateGame():
    global R1,R2,R3,C1,C2,C3,D1,D2,board,Game

    for restrictX in [1,2,3,4,6,7,8,9]:
        done = False
        prev = 0
        #while not done:
        Game = Running
        player = 1
        Mark = 'X'
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        R1 = []
        R2 = []
        R3 = []
        C1 = []
        C2 = []
        C3 = []
        D1 = []
        D2 = []
        
        # this function specifies the restriction on the player for the computer to win in the minimum number of moves

        if(restrictX==2):
            restrictO = 6
            firstMove = 9
        elif(restrictX==4):
            restrictO = 2
            firstMove = 3
        elif(restrictX==6):
            restrictO = 8
            firstMove = 7
        elif(restrictX==8):
            restrictO = 4
            firstMove = 1
        elif(restrictX==1):
            restrictO = 3
            firstMove = 6
        elif(restrictX==3):
            restrictO = 9
            firstMove = 8
        elif(restrictX==9):
            restrictO = 7
            firstMove = 4
        elif(restrictX==7):
            restrictO = 1
            firstMove = 2

        board[firstMove] = Mark
        splitBoard()
        player += 1
        start = 1
        rungame(board,'O',restrictX,restrictO)

# checks if the computer has won

def CheckWin1(board):
    global Game
    #Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    #Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=Win
    #Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=Win
    #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game=Running
        
# prints the current state of the board 

def printboard(board):
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")
    


def rungame(board,Mark,restrictX,restrictO):
    global Game
   
    if(Mark=='X'):
        cell = CheckWinIn1(restrictX)
        if(cell!=None):
            choice = cell
        else:
            cell = AvoidLossIn1(restrictX, restrictO)
            if (cell != None):
                choice = cell
            else:
               
                tf, cell = attack(restrictO, restrictX)
                if(tf):
                    choice = cell
                else:
                   
                    tf, cell = defend(restrictX)
                    if(tf):
                        choice = cell
                  
        board[choice] = Mark
        splitBoard()
        print("Restricted X in the below board: %s " % restrictX)
        print("Restricted O in the below board: %s " % restrictO)
        printboard(board)
        print("\n")
        
        CheckWin1(board)
        if(Game == Win):
            print ("The Computer wins")
            print("\n")
            board[choice]=' '
            return
        else:
            rungame(board,'O',restrictX,restrictO)
            board[choice] = ' '




    elif (Mark == 'O'):
        

        for choice in range(1,10):
            
            if (isValid(choice, restrictO)):
                if (CheckPosition(choice)):
                    board[choice] = Mark
                    splitBoard()
                    print("Restricted X in the below board: %s " % restrictX)
                    print("Restricted O in the below board: %s " % restrictO)
                    printboard(board)
                    print("\n")
                   
                    CheckWin1(board)
                    if(Game==Win):
                        print("Player win")
                        print("\n")
                        board[choice]=' '
                        return
                    else:
                        rungame(board,'X',restrictX,restrictO)
                        board[choice] = ' '
            
    return


#==================================================================================================
splitBoard()
simulateGame()
Game = Running
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("DONE!!!!")

print("Player 1 [X] --- Player 2 [O]\n")

print(" 1 | 2 | 3 ")
print("___|___|___")
print(" 4 | 5 | 6 ")
print("___|___|___")
print(" 7 | 8 | 9 ")
print("   |   |   ")


print("\n")
print ("********RULES*********\n")
print("1) You first choose, a cell where I can't play and then I do likewise \n")
print("2) Neither of us can block the centre cell(5) \n")
print("**********************\n")


restrictX = int(input("Enter a position where X cannot play : "))
while(restrictX==5):
    print("You cannot restrict the Centre Cell")
    restrictX = int(input("Enter a position where X cannot play : "))

if(restrictX==2):
    restrictO = 6
    firstMove = 9
elif(restrictX==4):
    restrictO = 2
    firstMove = 3
elif(restrictX==6):
    restrictO = 8
    firstMove = 7
elif(restrictX==8):
    restrictO = 4
    firstMove = 1
elif(restrictX==1):
    restrictO = 3
    firstMove = 6
elif(restrictX==3):
    restrictO = 9
    firstMove = 8
elif(restrictX==9):
    restrictO = 7
    firstMove = 4
elif(restrictX==7):
    restrictO = 1
    firstMove = 2

print("Thinking!!")
print("\n")
time.sleep(1)
board[firstMove] = Mark
splitBoard()
player += 1

while(Game == Running):
    os.system('cls')
    DrawBoard()
    print("\n")
    print("Restricted cell for X : %d " %(restrictX))
    print("Restricted cell for O : %d " % (restrictO))
    print("\n")


    choice=0

    if(player % 2 != 0):
        print("Player 1's chance(X)")
        Mark = 'X'
    else:
        print("Player 2's chance(O)")
        Mark = 'O'

    if(Mark=='X'):
        cell = CheckWinIn1(restrictX)
        if(cell!=None):
            choice = cell
        else:
            cell = AvoidLossIn1(restrictX, restrictO)
            if (cell != None):
                choice = cell
            else:
                
                tf, cell = attack(restrictO, restrictX)
                if(tf):
                    choice = cell
                else:
                    
                    tf, cell = defend(restrictX)
                    if(tf):
                        choice = cell
                  

        print ("Thinking!!")
        print("\n")
        time.sleep(0.25)
        board[choice] = Mark
        splitBoard()
        player += 1
        CheckWin()


    if (Mark == 'O'):
        choice = int(input("Enter the position between [1-9] where you want to mark : "))
        if (isValid(choice, restrictO)):
            if (CheckPosition(choice)):
                board[choice] = Mark
                splitBoard()
                player += 1
               
                CheckWin()
        else:
            print("\n")
            print("******You cannot play in a restricted cell******")
            print("\n")
            time.sleep(2)




os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw")
elif(Game==Win):
    player-=13
    if(player%2!=0):
        print("X Won\n)")
    else:
        print("O Won")


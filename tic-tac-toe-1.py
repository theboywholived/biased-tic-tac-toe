import random
#counts the number of moves played by 'X'
count = 0
#Stores the cell number of the previous move by either player or computer
prev_move = 0

#Returns a drawing of the board with the latest moves
def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#PLayer makes the move which is optimal
def makeMove(board, letter, move):
    board[move] = letter

#Checks whether player wins the game or not
#Returns true if player has won the game ; else false
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

#Returns a copy of the board with all the moves played
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

#Checks whether a particular cell is empty or not
#returns true if cell is empty;else false
def isSpaceFree(board, move):
    return board[move] == ' '

#Inputs the next move of the human player
#returns the cell number in which next move is played
def getPlayerMove(board):
    
    print("\nComputer's last move was " + str(prev_move))
    move = '0'
    print ("The restricted blocks are " + ",".join(str(i) for i in restrict(prev_move)))
    while int(move) not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not isSpaceFree(board, int(move)) or int(move) in restrict(
            prev_move):
       
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

#Checks all the possible positions which are available to play
#Returns a random move which is not restricted and empty;else returns none
def chooseRandmMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i) and i not in restrict(prev_move):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#Define : Cell number  [1,3,7,9] :Corner cell
#Define : Cell number  [2,4,6,8] :Edge cell
#Define : Cell number  [5] :Center cell

#If the First move 'X' is in a corner cell and second move 'O' is a edge cell
#Returns the next move to be played by computer to win
def AfterFirstMoveEdge(x):
    if x in [1, 3, 7, 9]:
        if x == 1:
            return random.choice([2, 4])
        elif x == 3:
            return random.choice([2, 6])
        elif x == 7:
            return random.choice([4, 8])
        elif x == 9:
            return random.choice([6, 8])

#If the First move 'X' is in a corner cell and second move 'O' is a corner cell along the same diagonal
#Returns the next move to be played by computer to win
def AfterFirstMoveDiagonal(x):
    if x in [1, 3, 7, 9]:
        if x == 1:
            return random.choice([3, 7])
        elif x == 3:
            return random.choice([1, 9])
        elif x == 7:
            return random.choice([1, 9])
        elif x == 9:
            return random.choice([3, 7])

#If the First move 'X' is in a corner cell and second move 'O' is a corner cell along the same row/column
#Returns the next move to be played by computer to win
def AfterFirstMoveRowColumn(x, y):
    if (x == 1 or x == 9):
        if (y == 3):
            return random.choice([7])
        elif (y == 7):
            return random.choice([3])
    elif (x == 3 or x == 7):
        if (y == 1):
            return random.choice([9])
        elif (y == 9):
            return random.choice([1])

#If there is a possibility to win in the very next move,play it
#Returns the cell number for immediate win
def EnsureImmediateWin(board):
    for i in range(1, 10):
        if i not in restrict(prev_move):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter):
                    return i

#If there is a possibility that the opponent can win in the next move,block it
#Returns the cell number which avoids immediate loss
def AvoidImmediateLoss(board):
    for i in range(1, 10):
        if i not in restrict(prev_move):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if isWinner(copy, playerLetter):
                    return i

#Restricts immediate adjacent row/column cells of the previous move
#Returns the list of restricted cells
def restrict(n):
    if n == 1:
        return [2, 4]
    elif n == 2:
        return [1, 3, 5]
    elif n == 3:
        return [2, 6]
    elif n == 4:
        return [1, 5, 7]
    elif n == 5:
        return [2, 4, 6, 8]
    elif n == 6:
        return [3, 5, 9]
    elif n == 7:
        return [4, 8]
    elif n == 8:
        return [5, 7, 9]
    elif n == 9:
        return [6, 8]
    else:
        return []

#Returns the next optimal move to be played by the computer
def getComputerMove(board, computerLetter):

    #Before computer plays its first move
    if (count == 0):  
        return random.choice([1, 3, 7, 9])

    #Before computer plays its second move    
    elif (count == 1):
        if (board.index('O') in [2, 4, 6, 8]):
            #If 'X' in corner and 'O' in edge
            return AfterFirstMoveEdge(board.index('X')) 
        if (board.index('O') in [1, 3, 7, 9]):
            if ((not isSpaceFree(theBoard, 1) and not isSpaceFree(theBoard, 9)) or (
                not isSpaceFree(theBoard, 3) and not isSpaceFree(theBoard, 7))):
                #If 'X' in corner and 'O' in corner along same diagonal
                return AfterFirstMoveDiagonal(board.index('X')) 
            else:
                #If 'X' in corner and 'O' along the corner in same row/column
                return AfterFirstMoveRowColumn(board.index('X'), board.index('O'))


        else:
            #Ensures win in next move if player wins in the next move
            if EnsureImmediateWin(board) != None:
                return EnsureImmediateWin(board)
            #Avoids immediate loss if opponent wins in the next move
            elif AvoidImmediateLoss(board) != None:
                return AvoidImmediateLoss(board)
            else:
            #Chooses a random move
                return chooseRandmMoveFromList(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])


    else:
        #Ensures win in next move if player wins in the next move
        if EnsureImmediateWin(board) != None:
            return EnsureImmediateWin(board)
        elif AvoidImmediateLoss(board) != None:
        #Avoids immediate loss if opponent wins in the next move
            return AvoidImmediateLoss(board)
        else:
            #Chooses a random move
            return chooseRandmMoveFromList(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#Checks whether all the cells in the board are full
#Returns true if Board if full;else false
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

#Start the game
print('Welcome to Tic Tac Toe!')


while True:
    theBoard = [' '] * 10 #Prints a empty board

    computerLetter = 'X' #Computer's move
    playerLetter = 'O' #PLayer's move
    gameIsPlaying = True #Checks state of game #Returns true is game is on;else false
    turn = 'computer'

    print ("\n\nWelcome to a new game\n")

    print ("*********************RULES***********************")

    print ("You cannot play in the immediate adjacent row/column cells of the previous player's last move")

    print ("**************************************************\n")

    print ("Enjoy the game!!!\n")

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard) #draws the board
            move = getPlayerMove(theBoard)  #Player's move
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter): 
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
            prev_move = int(move)

        else:
            move = getComputerMove(theBoard, computerLetter) #Computer's move
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
            count += 1
            prev_move = int(move)
    if (gameIsPlaying == False):
        print("Game Over , AI will take over")
        break




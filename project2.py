def main(): # [40% marks]
    # controls the flow of the program, allows the players to put their pieces and then move them,
    # alternately, if a mill is made, invites the player to remove opponents piece and decides which
    # player has won. Uses the random function for Player 2 (the computer) moves
def blocked(Occup, unOccup): [5% marks]
    # Occup is a list of occupied points/locations by a Player and unOccup are free locations
    # returns True if all pieces of the Player are blocked otherwise False
    return False
def movePiece(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup): # [30% marks]
    # this function performs a valid move for a Player (1 or 2) and updates the relevant lists
    # it uses the random function to make a valid move for Player 2 (the computer)
    # win is the GraphWin object, ptList is defined in drawBoard(), cColor is the color of pieces,
    # Occup is a list of occupied locations by the Player, linesOccup is a list of lines (mills)
    # by the Player, Circles is a list of the circles (pieces) and unOccup is a list of unOccup locations
    return [ ] # does not return anything
def drawBoard(win): # full code for this function is provided
    # draws the board and populates allLocs[ ] which contains all valid locations in ptList
    # returns ptList which is a 3x8 list of lists containing Point objects. 
def findNN(pt, ptList): # [5% marks]
    # finds the nearest location to a point pt in ptList so that the user is only required
    # to click near the location to place/select/move a piece and not exactly on top of it
    # returns the distance d and index location nn in ptList of the nearest point
    return nn, d
def isLine(Occup, linesOccup): # [10% marks]
    # Occup is a list of occupied locations by a Player and linesOccup are the Player's mills
    # returns True if a line (mill) has been made with the last move and updates linesOccup (mills)
    # otherwise returns False
    return False
   
def removePiece(win,ptList,Player,Occup,unOccup,linesOccup,Circles): # [10% marks]
    # performs the removal of a piece as per the game rules
    # and updates Occup, unOccup and Circles lists
    return [ ] # does not return anything

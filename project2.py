# CITS1401 Semester 1 2015, Project 2
# Student 1 Name: Bailey Moore  Student no:
# Student 2 Name: Samuel Heath  Student no: 21725083
# Twelve Men's Morris

from graphics import *

wSize = 600
allLocs = []

def main():
    # controls the flow of the program, allows the players to put their pieces and then move them,
    # alternately, if a mill is made, invites the player to remove opponents piece and decides which
    # player has won. Uses the random function for Player 2 (the computer)
    win = GraphWin('QAT',wSize,wSize)
    win.setBackground('green')
    win.setCoords(0,0,wSize,wSize)
    ptList = drawBoard(win)
    print(len(ptList), 'x', len(ptList[0]), "=", len(ptList)*len(ptList[0]))
    print(allLocs)

def blocked(Occup, unOccup):
    # Occup is a list of occupied points/locations by a Player and unOccup are free locations
    # returns True if all pieces of the Player are blocked otherwise False
    return False
    
def movePiece(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup):
    # this function performs a valid move for a Player (1 or 2) and updates the relevant lists
    # it uses the random function to make a valid move for Player 2 (the computer)
    # win is the GraphWin object, ptList is defined in drawBoard(), cColor is the color of pieces,
    # Occup is a list of occupied locations by the Player, linesOccup is a list of lines (mills)
    # of the Player, Circles is a list of the circles (pieces) and unOccup is a list of unOccup locations
    return [] # does not return anything

def drawBoard(win):
    # draws the board and populates the gobal list allLocs[] which contains all valid locations in ptList
    # returns ptList which is a 3x8 list of lists containing Point objects. At the top level it contains
    # the 3 squares (biggest first). At the second level, it contains the 8 Points that define
    # each square e.g. ptList[2][1] is the inner most square's 2nd Point. For each square, the bottom
    # left is the first Point
    bk = wSize/8
    ptList = []
    for i in range(1,4):
        ptList.append([Point(bk*i,bk*i), Point(bk*i,4*bk), Point(bk*i,bk*(8-i)),Point(4*bk,bk*(8-i)),
                       Point(bk*(8-i),bk*(8-i)),Point(bk*(8-i), 4*bk), Point(bk*(8-i),bk*i),Point(4*bk,bk*i)])
        pp = Polygon(ptList[-1])
        pp.setWidth(5)
        pp.setOutline(color_rgb(255,255,0))
        pp.draw(win)
        for j in range(8):
            allLocs.append([i-1,j])      
    for i in range(8):
        ll = Line(ptList[0][i],ptList[2][i])
        ll.setWidth(5)
        ll.setFill(color_rgb(255,255,0))
        ll.draw(win)
    return ptList 

def findNN(pt, ptList):
    # finds the nearest location to a point pt in ptList so that the user is only required
    # to click near the location to place/select/move a piece and not exactly on top of it
    # returns the distance d and index location nn in ptList of the nearest point
    return nn, d
    
def isLine(Occup, linesOccup):
    # Occup is a list of occupied locations by a Player and linesOccup are the Player's mills
    # returns True if a line (mill) has been made with the last move and updates linesOccup (mills)
    # otherwise returns False
    return False
  
def removePiece(win,ptList,Player,Occup,unOccup,linesOccup,Circles):
    # performs the removal of a piece as per the game rules
    # and updates Occup, unOccup and Circles lists
    return [] # does not return anything

def AImove(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup):
    # optional function for extra marks
    # replace the random function by this so that the computer (Player 2) performs an intelligent move
    return []
  
main()

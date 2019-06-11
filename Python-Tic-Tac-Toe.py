# Kody Kostboth and Riad (Ray) Shash
# CS410 FINAL PROJECT
# Spring 2017
#*****************************************************************************************************************************************
###The AI in this game is run like a simple automata. It makes its moves using a decision tree that has the following priorities:
###1. The AI will always make three in a row if such a move is possible.
###
###2. If the AI cannot make three in a row on this turn, and the player CAN make three in a row on their next turn, the AI will
###     place an 'O' in such a way that it blocks the player from completing their 3 in a row.
###
###2.5 If the player has more than one way to win in one turn, the AI will block whichever combination it comes accross first.
###
###3. If the player is not in a position to make 3 in a row on their next turn, and the AI cannot make 3 in a row on its current turn,
###	    the AI will attempt to place its symbol in a corner; given that it has LESS THAN THREE corner symbols already in place.
###
###4. If neither priority 1 or priority 2 evaluate to true, and the computer either cannot place its symbol in a corner, or it already is
###      in possession 3 corners, it will go through the table in 1 of 2 ways and place its 'O' in the first empty spot it can find.
# Import
import os       #For OS functions like clearing the screen
import time     #For time.... we will look into this later
import random   #To get random numbers... 

# Define the board (GLOBAL LIST)
# Indexes go from 1 to 9
# The 1st extra index is there to get rid of index 0...
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# The Slash screen of our game!
def print_introduction():
    os.system("cls")        #Clears the screen
    print("""
    
            Welcome to Kody's and Ray's Tic-Tac-Toe Game!
                         CS410 Final Project
                            SPRING 2017
""")
    time.sleep(2)  # Makes the computer wait for 2 seconds

# Print the header
def print_header():
    print("""           
These are the space number choices:
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9
  
  Pick a space from 1 to 9...
""")

#This clears the screen and shows the WIN message!
def print_win():
    os.system("cls")
    print("""--------------------------------------------------------------
	
                     CONGRATULATIONS! YOU WON! 
                        
--------------------------------------------------------------""")
	
def print_lose():
    os.system("cls")
    print("""--------------------------------------------------------------
                    OH NO! THE COMPUTER WON!
          Try again! I know there must be a way to win!
                        
--------------------------------------------------------------""")

def print_tie():
    os.system("cls")
    print("""--------------------------------------------------------------
                 IT LOOKS LIKE WE HAVE A DRAW!
        Please try again! You almost had it this time!
                      
--------------------------------------------------------------""")

# The print_board function
def print_board():
    print ("          |   |   ")
    print ("        " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print ("          |   |   ")
    print ("       ---|---|---")
    print ("          |   |   ")
    print ("        " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print ("          |   |   ")
    print ("       ---|---|---")
    print ("          |   |   ")
    print ("        " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print ("          |   |   ")
    print ()

def AI_move(numCornerOs):
#-----------------------------------------------------------------------------------------------------------------------------------------------#
                                                        ###Abreviated priority list###
#-----------------------------------------------------------------------------------------------------------------------------------------------#
                                        #   1.          Attempt to win with 3 in a row           #
                                        #   2. Attempt to block player from getting 3 in a row   #
                                        #   3.       Attempt to secure 3 of the 4 corners        #
                                        #   4.     Place an 'O' in the first available slot      #
#-----------------------------------------------------------------------------------------------------------------------------------------------#
                              ###The full descriptive priority list can be found at the top of the program###
#-----------------------------------------------------------------------------------------------------------------------------------------------#

    if(board[2] == 'O' and board[3] == 'O' and board[1] != 'X'): #Check for all combinations of 2, and add a 3rd if possible
        board[3] == 'O'
    elif(board[1] == 'O' and board[3] == 'O' and board[2] != 'X'):
        board[2] = 'O'
    elif(board[4] == 'O' and board[6] == 'O' and board[5] != 'X'):
        board[5] = 'O'
    elif(board[7] == 'O' and board[9] == 'O' and board[8] != 'X'):
        board[8] = 'O'
    elif(board[1] == 'O' and board[7] == 'O' and board[4] != 'X'):
        board[4] = 'O'
    elif(board[2] == 'O' and board[8] == 'O' and board[5] != 'X'):
        board[5] = 'O'
    elif(board[3] == 'O' and board[9] == 'O' and board[6] != 'X'):
        board[6] = 'O'
    elif(board[1] == 'O' and board[9] == 'O' and board[5] != 'X'):
        board[5] = 'O'
    elif(board[3] == 'O' and board[7] == 'O' and board[5] != 'X'):
        board[5] = 'O'
    elif(board[1] == 'O' and board[2] == 'O' and board[3] != 'X'):
        board[3] = 'O'
    elif(board[4] == 'O' and board[5] == 'O' and board[6] != 'X'):
        board[6] = 'O'
    elif(board[7] == 'O' and board[8] == 'O' and board[9] != 'X'):
        board[9] = 'O'
    elif(board[2] == 'O' and board[3] == 'O' and board[1] != 'X'):
        board[1] = 'O'
    elif(board[5] == 'O' and board[6] == 'O' and board[4] != 'X'):
        board[4] = 'O'
    elif(board[8] == 'O' and board[9] == 'O' and board[7] != 'X'):
        board[7] = 'O'
    elif(board[1] == 'O' and board[4] == 'O' and board[7] != 'X'):
        board[7] = 'O'
    elif(board[2] == 'O' and board[5] == 'O' and board[8] != 'X'):
        board[8] = 'O'
    elif(board[3] == 'O' and board[6] == 'O' and board[9] != 'X'):
        board[9] = 'O'
    elif(board[4] == 'O' and board[7] == 'O' and board[1] != 'X'):
        board[1] = 'O'
    elif(board[5] == 'O' and board[8] == 'O' and board[2] != 'X'):
        board[2] = 'O'
    elif(board[6] == 'O' and board[9] == 'O' and board[3] != 'X'):
        board[3] = 'O'
    elif(board[3] == 'O' and board[6] == 'O' and board[9] != 'X'):
        board[9] = 'O'
    elif(board[1] == 'O' and board[5] == 'O' and board[9] != 'X'):
        board[9] = 'O'
    elif(board[3] == 'O' and board[5] == 'O' and board[7] != 'X'):
        board[7] = 'O'
    elif(board[7] == 'O' and board[5] == 'O' and board[3] != 'X'):
        board[3] = 'O'
    elif(board[9] == 'O' and board[5] == 'O' and board[1] != 'X'):
        board[1] = 'O' #This is the last move! With this, it'll be able to finish just about any combination
    elif(board[1] == 'X' and board[3] == 'X' and board[2] != 'O'): #Attempt to block any combinations of 2 that the player has.
        board[2] = 'O'                                             #The AI will search for all X's in any "Almost winning order" and respond accordingly
    elif(board[4] == 'X' and board[6] == 'X' and board[5] != 'O'):
        board[5] = 'O'
    elif(board[7] == 'X' and board[9] == 'X' and board[8] != 'O'):
        board[8] = 'O'
    elif(board[1] == 'X' and board[7] == 'X' and board[4] != 'O'):
        board[4] = 'O'
    elif(board[2] == 'X' and board[8] == 'X' and board[5] != 'O'):
        board[5] = 'O'
    elif(board[3] == 'X' and board[9] == 'X' and board[6] != 'O'):
        board[6] = 'O'
    elif(board[1] == 'X' and board[9] == 'X' and board[5] != 'O'):
        board[5] = 'O'
    elif(board[3] == 'X' and board[7] == 'X' and board[5] != 'O'):
        board[5] = 'O'
    elif(board[1] == 'X' and board[2] == 'X' and board[3] != 'O'):
        board[3] = 'O'
    elif(board[4] == 'X' and board[5] == 'X' and board[6] != 'O'):
        board[6] = 'O'
    elif(board[7] == 'X' and board[8] == 'X' and board[9] != 'O'):
        board[9] = 'O'
    elif(board[2] == 'X' and board[3] == 'X' and board[1] != 'O'):
        board[1] = 'O'
    elif(board[5] == 'X' and board[6] == 'X' and board[4] != 'O'):
        board[4] = 'O'
    elif(board[8] == 'X' and board[9] == 'X' and board[7] != 'O'):
        board[7] = 'O'
    elif(board[1] == 'X' and board[4] == 'X' and board[7] != 'O'):
        board[7] = 'O'
    elif(board[2] == 'X' and board[5] == 'X' and board[8] != 'O'):
        board[8] = 'O'
    elif(board[3] == 'X' and board[6] == 'X' and board[9] != 'O'):
        board[9] = 'O'
    elif(board[4] == 'X' and board[7] == 'X' and board[1] != 'O'):
        board[1] = 'O'
    elif(board[5] == 'X' and board[8] == 'X' and board[2] != 'O'):
        board[2] = 'O'
    elif(board[6] == 'X' and board[9] == 'X' and board[3] != 'O'):
        board[3] = 'O'
    elif(board[3] == 'X' and board[6] == 'X' and board[9] != 'O'):
        board[9] = 'O'
    elif(board[1] == 'X' and board[5] == 'X' and board[9] != 'O'):
        board[9] = 'O'
    elif(board[3] == 'X' and board[5] == 'X' and board[7] != 'O'):
        board[7] = 'O'
    elif(board[7] == 'X' and board[5] == 'X' and board[3] != 'O'):
        board[3] = 'O'
    elif(board[9] == 'X' and board[5] == 'X' and board[1] != 'O'):
        board[1] = 'O'
    elif(board[1] != 'X' and board[1] != 'O' and numCornerOs[0] < 3): #The AI tries from here downward to try and place its 'O' in a corner....
        board[1] = 'O'
        numCornerOs[0] += 1            #....But only if it doesn't already have 3 corners
    elif(board[3] != 'X' and board[3] != 'O' and numCornerOs[0] < 3):
        board[3] = 'O'
        numCornerOs[0] += 1
    elif(board[7] != 'X' and board[7] != 'O' and numCornerOs[0] < 3):
        board[7] = 'O'
        numCornerOs[0] += 1
    elif(board[9] != 'X' and board[9] != 'O' and numCornerOs[0] < 3):
        board[9] = 'O'
        numCornerOs[0] += 1 #and just like that, we've covered all four corners. Now we try to connect our three corners. It will usually do this by blocking any attempt the player is making at their own victory!
    else: #The loop will only get here if the AI has no moves to win with and no player moves to block
        randumb = False #boolean used to check if I've played anything yet
        if(random.random() > .5): #To make things a little more interesting, I'll allow the ai to move through the list backwards at time!(specifically, if random <= .5
            counter = 1 #used to iterate through my list
            while randumb == False:
                if(board[counter] != 'X' and board[counter] != 'O'):
                    board[counter] = 'O' #make my move
                    randumb = True #tell the computer I've made my move
                else: #I didn't make my move because the space was full, so let's check the next space
                    counter += 1
        else:
            counter = 9 #used to iterate through my list
            while randumb == False:
                if(board[counter] != 'X' and board[counter] != 'O'):
                    board[counter] = 'O' #make my move
                    randumb = True #tell the computer I've made my move
                else: #I didn't make my move because the space was full, so let's check the next space
                    counter -= 1

#This function checks if the player won the game. There are 8 ways to win...
def checkplayerwin():
    if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
        (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or \
        (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or \
        (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or \
        (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
        (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
        (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or \
        (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
            return True
    else:
        return False

#This function checks if the player lost the game. Just like there are 8 ways to win, there are 8 ways to lose
def checkplayerloose():
    if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or \
        (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or \
        (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or \
        (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or \
        (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
        (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
        (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or \
        (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
            return True
    else:
        return False

def checkfortie():
    checkTie = True #This variable will be set to false if the following loop finds an element in the table that is not an X or an O
    for element in board:
        if element == " ":
            checkTie = False
    return checkTie

def main():
    whoGoesFirst = True #Will be set in the upcoming loop. If true, player goes first. If False, computer goes first
    print_introduction()
    os.system("cls")
    print("""------------------------------------------------------------------------
	
                     Let's flip a coin!
                        
------------------------------------------------------------------------""")
    time.sleep(2)
    print(" It's flipping in the air! You'll get to go first if it lands on Heads!")
    time.sleep(3)
    
    #Random number
    coinFlipNumber = int(random.random() * 20) + 12
    
    for x in range(0, coinFlipNumber):
        if(whoGoesFirst == True):
            print("   T")
            time.sleep(.15)
            whoGoesFirst = False
        else:
            print("   H")
            time.sleep(.15)
            whoGoesFirst = True
            
    if(whoGoesFirst == True):
        print("It looks like it landed on heads! You get to go first!")
        time.sleep(5)
        os.system("cls")
        numCornerOs = [0] #used to keep track of how many corner spots the AI has taken
        invalidMove = False #Used to make sure the AI doesn't make a move after an invalid move
        numMoves = 0
        playgame = True             #Bool for... are we playing the game?

        # While the game is running... (We can change this later)...
        while (playgame == True):
            # Clears the terminal screen
            os.system("cls")

            # Shows the splash screen of our game!
            print_header()
            print_board()
		    #Runs the function to check if the player won
            didplayerwin = checkplayerwin()
            #Check if the player won the game

            #Runs the function to check if the computer won
            didplayerlose = checkplayerloose()
            if (didplayerwin == True):
                playgame == False
                print_win()
                time.sleep(10)
                break #Exits the loop because the game is over
            if(didplayerlose == False and didplayerwin == False and numMoves >=9): #Check for a tie! But only after 9 moves, because then the board will be full.
                playgame == False
                print_tie()
                time.sleep(10)
                break #exit the loop! The game is over and it's time to try again

            if(numMoves > 0 and invalidMove == False): #To be totaly honest, I could probably have gotten rid of a lot of code duplication by expanding on this statement instead of redoing everything for the computer to go first. But that's ok! I'll be a little lazy!!
                print("I am making my move!")
                time.sleep(1.5)
                AI_move(numCornerOs)
                os.system("cls")
                print_header()
                print_board()
                numMoves += 1

            #Runs the function to check if the player won again, just to be sure before I check for a tie
            didplayerwin = checkplayerwin()
            #Runs the function to check if the computer won
            didplayerlose = checkplayerloose()
    
            if(didplayerlose == True): #Check and see if the player lost
                time.sleep(2)
                playgame == False
                print_lose()
                time.sleep(10)
                break #exit the loop because they lost and the game is over!
 
            choice = input("Please choose an empty space for X and press enter: ")
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------             
            #Exception Handling (tries to convert to int)
            try:
                choice = int(choice)  # Convert to integer 
            except ValueError:
                print("Sorry, Invalid move!")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
                continue  # Continue with the loop, but not exit the loop!
                
            # If the user enters a choice that is out of the range of 1-9
            if (choice < 1 or choice > 9):
                print("Sorry, Invalid move!")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
                continue  # Continue with the loop, but not exit the loop!

            # Check to see if the space is empty
            if board[choice] == " ":
                invalidMove = False #It was not an invalid move, so we make this false. This will let the computer have it's turn.
                board[choice] = "X"
                numMoves += 1
            else:
                print("Sorry, Invalid move. Try again...")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
#------------------------------------------------------------------------------------------------------------------------------------------------------- 
    else: #Now we go through and let the computer go first!
        print("The coin came up Tails! We'll let the computer go first!")
        time.sleep(5)
        os.system("cls")
        numCornerOs = [0] #used to keep track of how many corner spots the AI has taken
        invalidMove = False #Used to make sure the AI doesn't make a move after an invalid move
        numMoves = 0
        playgame = True             #Bool for... are we playing the game?

        # While the game is running... (We can change this later)...
        while (playgame == True):
            # Clears the terminal screen
            os.system("cls")

            # Shows the splash screen of our game!
            print_header()
            print_board()
		    #Runs the function to check if the player won
            didplayerwin = checkplayerwin()
            #Check if the player won the game
            if (didplayerwin == True):
                playgame == False
                print_win()
                time.sleep(10)
                break #Exits the loop because the game is over
            if(invalidMove == False):
                print("I am making my move!")
                time.sleep(1.5)
                AI_move(numCornerOs)
                os.system("cls")
                print_header()
                print_board()
                numMoves += 1

            #Runs the function to check if the player won again, just to be sure before I check for a tie
            didplayerwin = checkplayerwin()
            #Runs the function to check if the computer won
            didplayerlose = checkplayerloose()
    
            if(didplayerlose == True): #Check and see if the player lost
                time.sleep(2)
                playgame == False
                print_lose()
                time.sleep(10)
                break #exit the loop because they lost and the game is over!
       
            if(didplayerlose == False and didplayerwin == False and numMoves >=9): #Check for a tie! But only after 9 moves, because then the board will be full.
                playgame == False
                print_tie()
                time.sleep(10)
                break #exit the loop! The game is over and it's time to try again
 
            choice = input("Please choose an empty space for X and press enter: ")
            choice = int(choice)  # Convert to integer (I will use exception handling later...)
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------            
            #Exception Handling (tries to convert to int)
            try:
                choice = int(choice)  # Convert to integer 
            except ValueError:
                print("Sorry, Invalid move!")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
                continue  # Continue with the loop, but not exit the loop!

            # If the user enters a choice that is out of the range of 1-9
            if (choice < 1 or choice > 9):
                print("Sorry, Invalid move!")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
                continue  # Continue with the loop, but not exit the loop!

            # Check to see if the space is empty
            if board[choice] == " ":
                invalidMove = False #It was not an invalid move, so we make this false. This will let the computer have it's turn.
                board[choice] = "X"
                numMoves += 1
            else:
                print("Sorry, Invalid move. Try again...")
                invalidMove = True
                time.sleep(1)  # Makes the computer wait for 1 second
#------------------------------------------------------------------------------------------------------------------------------------------------------- 
#Runs the game!
main()

#   GLOBAL VARIABLES

current_player = "X"

game_still_going = True

winner = None

# Making board for game 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

def play_game():

  display_board()
  
  # Loop until the game stops (winner or tie)
  while game_still_going:
    # Handle a single turn of a arbitrary player
    handle_turn(current_player)

    check_if_game_over() 
    
    # flip to other player
    flip_current_player()
  
  # Since the game is over, print the winner or tie 
  if winner == "X" or winner == "O":
    print(winner+' is the winner !!') 
  elif winner == None:
    print('Tie !! Game is over ')  

# Display the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] +"    1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] +"    4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] +"    7 | 8 | 9")     

# Handle a turn for an arbitrary player
def handle_turn(current_player):

  # Get position from player
  print(current_player+"'s turn")
  position = input("Choose a position from 1-9 : ")
  
  # Make sure input is valid and space is empty
  valid = False   
 
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position from 1-9 : ")

    # As for list , indexing starts from 0
    position = int(position) - 1  

    # Then also make sure the spot is available on the board
    if board[position] == "-" :
      valid = True
    else:   
      print("You can't enter there . It is already filled")

  board[position] = current_player
  display_board()


def check_if_game_over():
  check_if_win() 
  check_if_tie()    

def check_if_win():
  # Set global variables
  global winner
  # Check rows
  row_winner = check_row()
  # Check columns
  column_winner  = check_column()
  # Check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner

  elif column_winner:
    winner = column_winner

  elif diagonal_winner:
    winner = diagonal_winner

  else:
    # There is no win       
    winner = None
 

def check_row():

  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row1 = board[0] == board[1] == board[2] !="-"
  row2 = board[3] == board[4] == board[5] !="-"
  row3 = board[6] == board[7] == board[8] !="-" 
  
  # If any row does have a match, flag that there is a win
  if row1 or row2 or row3:
    # Game ends
    game_still_going = False
  
  # return the winner X or O
  if row1:
    return board[0]

  elif row2:
    return board[3]  

  elif row3:
    return board[6] 
  # If there is no winner 
  else:
    return None   
 

def check_column():
  global game_still_going

  column1 = board[0] == board[3] == board[6] !="-"
  column2 = board[1] == board[4] == board[7] !="-"
  column3 = board[2] == board[5] == board[8] !="-" 
  
  if column1 or column2 or column3:
    # Game ends
    game_still_going = False
   
  # return the winner X or O
  if column1:
    return board[0]

  elif column2:
    return board[1]  

  elif column3:
    return board[2] 

  else:
    return None   


def check_diagonals():
  global game_still_going

  diagonal1 = board[0] == board[4] == board[8] !="-"
  diagonal2 = board[2] == board[4] == board[6] !="-"
  
  if diagonal1 or diagonal2 :
    # Game ends
    game_still_going = False  
  
  # return the winner X or O
  if diagonal1:
    return board[0]

  elif diagonal2:
    return board[2]  
 
  else:
    return None   
   

def check_if_tie():
  global game_still_going
  # No one is the winner # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie   
  else:
    return False    

# Flip the current player from X to O, or O to X
def flip_current_player():
  global current_player

  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"  

# ------------ Start Execution -------------
# Lets play the game of tic tac toe
play_game()  

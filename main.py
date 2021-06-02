# dic for user inputs and valid movements
dic = {"A1" : 0, "A2": 3, "A3": 6, "B1" : 1, "B2": 4, "B3": 7, "C1" : 2, "C2": 5, "C3": 8}

def create_board():
    return ["-"]*9

def is_winer(board, player):
    # check rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    #check columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[5] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    #check diagonals
    if board[0] == board[4] == board[5] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_board_fill(board):
    if "-" in board: 
        return False
    else:
        return True

def print_board(board):
    print("-------------")
    print("Board:")
    print("    A   B   C\n")
    print("1   " + board[0] + "   " +  board[1] + "   " +  board[2])
    print("2   " + board[3] + "   " +  board[4] + "   " +  board[5])
    print("3   " + board[6] + "   " +  board[7] + "   " +  board[8])
    print("-------------\n")
    
def check_correct_move(board, position):
    if(board[position] == "-"):
        return True
    else:
        return False

def get_position():
    while True:
        position = input("Select position (example A1): ").upper()
        print("Position selected: " + position)
        if (position in dic) and (dic[position] != -1):
            position_to_insert = dic[position]
            dic[position] = -1 # now this position is not valid  
            return position_to_insert
        else:
            print("Invalid position! Try again!")

if __name__ == "__main__":
    board = create_board()
    player_control = 2
    is_draw = False 
    while not is_board_fill(board):
        print_board(board)
        move = get_position()
        player = "X" if player_control % 2 == 0 else "O"
        board[move] = player
        
        #check if win
        if(is_winer(board, player)):
            print_board(board)
            print("\nWINNER: " + player)
            break
        
        player_control += 1 #next turn

    if is_draw:
        print("DRAW!\nBoard results:")
        print_board(board)


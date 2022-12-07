#program : tic-tac-toe game 

#author : stone-kay

board = [1,2,3,4,5,6,7,8,9]
currentToken = "X"
winningToken = ""
slotsfilled = 0

print("tic-tac-toe by stonekay")
print("Match three lines vertically horizontally or diagonally")
print("X goes first then O")

while winningToken =="" and slotsfilled < 9:
    print("\n")
    print("%s|%s|%s" % (board[0], board[1] , board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")

    print("%s|%s|%s" % (board[6], board[7], board[8]))

    position = -1 
    
    while (position == -1) :
        position = int(input("\n%s's turn. Where to: " %currentToken))

        if (position < 1) or (position > 9):
            position = -1
            print("position should be between 1 and 9")
        
        position = position - 1

        if board[position] == "X" or board[position] == "O":
            print("position has already been taken")
            positon = -1 

    board[position] = currentToken
    slotsfilled += 1 

    #ROW CHECKING 

    row_1 = board[0] == currentToken and board[1] ==currentToken and board[2] == currentToken
    row_2 = board[3] == currentToken and board[4] == currentToken and board[5] == currentToken
    row_3 = board[6] ==currentToken and board[7] == currentToken and board[8] == currentToken

    #COLLUM CHECKIING 

    col_1  = board[0]==currentToken and board[3]==currentToken and board[6] == currentToken
    col_2  = board[1] ==currentToken and board[4] ==currentToken and board[7] == currentToken 
    col_3  = board[2] ==currentToken and board[5] ==currentToken  and board[8] == currentToken

    #diagonal checking 
    diag_1  = board[0] ==currentToken and board[4] and board[8] == currentToken 
    diag_2 = board[2] ==currentToken and board[4] and board[6] == currentToken

    row = row_1 or row_2 or row_3
    col = col_1 or col_2 or col_3
    diag = diag_1 or diag_2
    
    if(row or col or diag):
        
        print("\n")
        print("%s|%s|%s" % (board[0], board[1], board[2]))
        print("-+-+-")
        print("%s|%s|%s" % (board[3], board[4], board[5]))
        print("-+-+-")
        print("%s|%s|%s" % (board[6], board[7], board[8]))

        print(f"congrations you have player {currentToken} ")
        winningToken = currentToken
    if currentToken == "X":
        currentToken = "O"
    else:
        currentToken = "X"

if slotsfilled == 9 and winningToken =="":
    print("No one won  :( Better luck players ")
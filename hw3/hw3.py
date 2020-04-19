# *************** EXERCISE 3 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def is_not_dup(lst):#checks if a list has duplicate number
    lstcount = [0]*10
    for i in range(len(lst)):
        if lst[i]!=0:
            lstcount[lst[i]]=lstcount[lst[i]]+1
    for j in range(len(lstcount)):
        if lstcount[j]>1:
            return False
    return True
def block(board,row,col):#checks if a block has duplicate number
    lst = []
    for srow in range(3*(row//3),3*(row//3)+3):
        for scol in range(3*(col//3),3*(col//3)+3):        
            lst.append(board[srow][scol])
    if is_not_dup(lst) == False:
        return False
    return True
def is_not_dup_board(board):#checks if a list of lists has duplicate number
    i = 0
    for i in range(len(board[i])):#checks duplicates in rows
        if is_not_dup(board[i])==False:
            return False
    lstcol = []
    for row in range(len(board)):#checks duplicates in cols
        for col in range(len(board[row])):
            lstcol.append(board[col][row])
        if is_not_dup(lstcol)==False:
            return False
        lstcol = []
    for row in range(0,len(board),3):#checks duplicates in blocks
        for col in range(0,len(board[row]),3):
            if block(board,row,col)==False:
                return False
    return True

def is_valid_sudoku_board(board):
    """gets a list of lists and checks if the board is valid sudoku board"""
    if type(board)!=list:#checks that the Type of the board is list
        return False
    for i in range(len(board)):
        if type(board[i])!=list:#checks that the Type of a row is list
            return False
        if len(board[i])!=9:#checks that the Number of numbers in a row is 9
            return False
    if len(board)!=9:#checks that the number of rows is 9
        return False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if type(board[row][col])!=int or board[row][col]>9 or board[row][col]<0:#checks that the Type and the value is valid
                return False
    if is_not_dup_board(board)== False:#checks if every block col and row has duplicate numbers
        return False
    return True

def is_valid_move(board,row,col,digit):
    """gets a sudoko board, number of row and col and checks if you can insert your digit"""
    if(is_valid_sudoku_board(board)==False):
        return False
    if row>8 or row<0 or col>8 or col<0 or digit<1 or digit>9:#checks that the row, col, digit is valid
        return False
    if board[row][col]!=0:#checks that you are trying to insert your digit to a valid place
        return False
    for i in range(len(board)):
        if board[row][i]==digit:#checks that your digit isn't in the row
            return False
        if board[i][col]==digit:#checks that your digit isn't in the col
            return False
    for srow in range(3*(row//3),3*(row//3)+3):
        for scol in range(3*(col//3),3*(col//3)+3):        
            if board[srow][scol]==digit: #checks that your digit isn't in the block
                return False
    return True

def enter_digit(board,row,col,digit):
    """gets a sudoko board, number of row and col and insert the digit in the right place if its a valid move"""
    if is_valid_move(board,row,col,digit):
        board[row][col]=digit
        return True
    return False
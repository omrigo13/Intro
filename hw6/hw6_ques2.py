# *************** EXERCISE 6 ***************

# **************************************************************
# ************************ QUESTION 2 **************************
FREE_CELL = "*"
OCCUPIED_CELL = "#"
BLOCK_CELL = "B"
 
def rec_fill_domino(board, row_index, col_index):
    """
    gets a board of *,# and fills the cells with * with B blocks of size 2 like
    domino board
    :param list board: a list of lists represents a given domino board
    :param int row_index: integer represents the index of the row in the board
    :param int col_index: integer represents the index of the column in the board
    :return: return True if there is a solution to solve the board and False 
    otherwise
    :rtype: bool
    """
    if col_index == len(board[row_index]) - 1 and row_index == len(board) - 1:#base case
        return True
 
    if board[row_index][col_index] != FREE_CELL:#checks if the cell free or not
        if col_index != len(board[row_index]) - 1:
            return rec_fill_domino(board, row_index, col_index + 1)#recursive call
        else:
            return rec_fill_domino(board, row_index + 1, 0)#recursive call
 
    board[row_index][col_index] = BLOCK_CELL#replace a free cell to block cell
    if col_index == len(board[row_index]) - 1:
        if board[row_index + 1][col_index] == FREE_CELL:#replace a free cell to block cell - down
            board[row_index + 1][col_index] = BLOCK_CELL
        else:
            board[row_index][col_index] = FREE_CELL
            return False
    elif row_index == len(board) - 1:
        if board[row_index][col_index + 1] == FREE_CELL:#replace a free cell to block cell - right
            board[row_index][col_index + 1] = BLOCK_CELL
        else:
            board[row_index][col_index] = FREE_CELL
            return False
    else:
        if board[row_index + 1][col_index] == FREE_CELL:#replace a free cell to block cell - down
            board[row_index + 1][col_index] = BLOCK_CELL
            if not rec_fill_domino(board, row_index, col_index):#wrong move - return one step back
                board[row_index + 1][col_index] = FREE_CELL
            else:
                return True
        if board[row_index][col_index + 1] == FREE_CELL: #replace a free cell to block cell - right
            board[row_index][col_index + 1] = BLOCK_CELL
            if not rec_fill_domino(board, row_index, col_index):#wrong move - return one step back
                board[row_index][col_index] = FREE_CELL
                board[row_index][col_index + 1] = FREE_CELL
                return False
        else:
            board[row_index][col_index] = FREE_CELL#wrong move - return one step back
            return False
    return rec_fill_domino(board, row_index, col_index)#recursive call
 
 
 
def domino_problem(board):
    """
    :param list board: a domino board of * represents free cells and # 
    represents occupied cells. hould check if it can be filled with B blocks 
    to solve the domino board
    :return: list that represents the solution for a domino board if its possible
    otherwise str Broken board
    :rtype: list for True and str for False
    """
    if rec_fill_domino(board, 0, 0):
        return board
    return "Broken board"
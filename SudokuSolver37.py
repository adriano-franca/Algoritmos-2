def solveSudoku(board):
    lines = [ set() for _ in range(9) ]
    cols  = [ set() for _ in range(9) ]
    subs  = [ set() for _ in range(9) ]
    
    def index_sub(lin, col):
        return (lin//3)*3 + col//3
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.': continue
            num = int(board[i][j])
            lines[i].add(num)
            cols[j].add(num)
            subs[index_sub(i,j)].add(num)
      
    def can_play(lin, col, num):
        if num in lines[lin]: return False
        if num in cols[col]: return False
        if num in subs[index_sub(lin,col)]: return False
        return True

    def backtracking(lin, col):
        if lin>=9: 
            return True #sudoku is filled
        next_lin = lin if col<8 else lin+1
        next_col = col+1 if col<8 else 0
        if board[lin][col]!='.':
            return backtracking(next_lin, next_col)
        else: # '.'
            for i in range(9,0,-1):
                if can_play(lin,col,i):
                    board[lin][col] = str(i)
                    lines[lin].add(i)
                    cols[col].add(i)
                    subs[index_sub(lin,col)].add(i)
                    if backtracking(next_lin,next_col):
                        return True
                    board[lin][col] = "."
                    lines[lin].remove(i)
                    cols[col].remove(i)
                    subs[index_sub(lin,col)].remove(i)
            return False
    backtracking(0,0)

#Caso de teste
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)
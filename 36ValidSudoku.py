def isValidSudoku(board) -> bool:
    lines = [ set() for _ in range(9) ]
    cols  = [ set() for _ in range(9) ]
    subs  = [ set() for _ in range(9) ]

    def index_sub(lin, col):
        return (lin//3)*3 + col//3

    for i in range(9):
        for j in range(9):
            if board[i][j]=='.': continue
            num = int(board[i][j])
            if num not in lines[i]:
                lines[i].add(num)
            else:
                return False
            if num not in cols[j]:
                cols[j].add(num)
            else:
                return False
            if num not in subs[index_sub(i,j)]:
                subs[index_sub(i,j)].add(num)
            else:
                return False
            
    return True
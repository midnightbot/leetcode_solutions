class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        ## the square is E open the adjacent cells that are B
        ## if press on mine 'm' change it to 'x' and game over
        ## if E has a mine adjacent chnage it to number of adjacent mines
        r = click[0]
        c = click[1]
        n = len(board)
        m = len(board[0])

        if board[r][c] == 'M': ## mine case handeled
            board[r][c] = 'X'
            return board

        def valid(x,y):  ## find if a coordinate is valid or not
            return 0<=x<n and 0<=y<m

        ## find nei of a coordinate and mine count near it
        def find_nei(x,y):
            nei = []
            ops = [[0,+1], [0,-1], [-1,-1], [-1,0], [-1,+1], [+1,-1], [+1,0], [+1,+1]]
            mine_count = 0
            for it in ops:
                new_x,new_y = x+it[0], y+it[1]
                if valid(new_x,new_y):
                    nei.append([new_x,new_y])
                    if board[new_x][new_y] == 'M':
                        mine_count+=1

            return nei, mine_count

        ## update the board according to the given rules
        def upd_board(r,c):
            if board[r][c] not in '1234567890BX':
                neis, mines = find_nei(r,c)
                if mines == 0:
                    board[r][c] = 'B'
                    for it in neis:
                        upd_board(it[0], it[1])
                else:
                    board[r][c] = str(mines)

        upd_board(r,c)
        return board



class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        ## 3 or more same candies horizontallu or vertically
        ## drop candies until empty is filled below it

        m = len(board)
        n = len(board[0])
        def check_horizontal(board):
            rows = {x:set() for x in range(m)}
            for indx, r in enumerate(board):
                for it in range(2, n):
                    if r[it] == r[it-1] == r[it-2]:
                        rows[indx].add(it)
                        rows[indx].add(it-1)
                        rows[indx].add(it-2)

            return rows

        def check_vertical(board):
            cols = {x:set() for x in range(n)}
            for x in range(2, m):
                for y in range(0,n):
                    if board[x][y] == board[x-1][y] == board[x-2][y]:
                        cols[y].add(x)
                        cols[y].add(x-1)
                        cols[y].add(x-2)
            return cols

        def do_updates(board, rows, cols):
            updates = 0
            for it in rows:
                for c in rows[it]:
                    board[it][c] = 0
                    updates+=1

            for it in cols:
                for r in cols[it]:
                    board[r][it] = 0
                    updates+=1
            return updates

        def drop_candies(board):
            board = [x for x in zip(*board)]
            ans = []

            for r in board:
                temp = []
                for it in r:
                    if it!=0:
                        temp.append(it)
                diff = m - len(temp)
                diff = [0 for x in range(diff)]
                temp = diff + temp

                ans.append(temp)
            #print([x for x in zip(*ans)])
            return [list(x) for x in zip(*ans)]

        upds = 1
        count = 0
        while count!=100:
            ans = check_horizontal(board)
            ans2 = check_vertical(board)
            upds = do_updates(board,ans,ans2)
            board = drop_candies(board)
            count+=1
            #print(upds)

        return board

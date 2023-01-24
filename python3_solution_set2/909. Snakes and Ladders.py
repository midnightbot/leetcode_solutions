class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        ## simple bfs

        n = len(board)
        def find_pos(num):
            '''
            Finds position of a num on the board
            '''
            r,c = divmod(num-1, n)
            if r%2==0:
                return n-r-1,c
            else:
                return n-r-1,n-c-1

        seen = set()
        q = [(1,0)]

        while q:

            nums, steps = q.pop(0)
            r,c = find_pos(nums)

            if board[r][c]!=-1:
                nums = board[r][c]
            if nums == n**2:
                return steps
            for x in range(1,7):
                new_nums = nums + x
                if new_nums <= n**2 and new_nums not in seen:
                    seen.add(new_nums)
                    q.append((new_nums, steps+1))


        return -1

        

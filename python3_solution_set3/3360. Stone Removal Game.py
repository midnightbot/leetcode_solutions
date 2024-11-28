class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        size = 10
        turn = 0

        while n!=0:
            if n >= size:
                n-=size
                size-=1
                turn = (turn+1)%2

            else:
                return turn == 1

        return turn == 1
        

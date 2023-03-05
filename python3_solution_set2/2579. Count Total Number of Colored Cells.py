class Solution:
    def coloredCells(self, n: int) -> int:

        sq_side = (2*n-1)
        total = sq_side * sq_side

        up_side = (sq_side-1)//2
        not_color = sum([x+1 for x in range(up_side)])

        return total - not_color*4

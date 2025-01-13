class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        arr = []

        for indx,x in enumerate(grid):
            if indx%2==0:
                arr += x
            else:
                arr += x[::-1]
        
        return [arr[x] for x in range(0,len(arr),2)]

        
        

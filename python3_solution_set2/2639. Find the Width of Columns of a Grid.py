class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        grid = [x for x in zip(*grid)] ## col to row conversion
        ans = []

        for it in grid:
            lens = 0
            for x in it:
                lens = max(lens, len(str(x)))
            ans.append(lens)

        return ans

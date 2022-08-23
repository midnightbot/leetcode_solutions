class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def cnts(arr):
            return arr.count('W')
        ans = float('inf')
        for x in range(0,len(blocks)-k+1,+1):
            ans = min(ans, cnts(blocks[x:x+k]))
        return ans
        
        

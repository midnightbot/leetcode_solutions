class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        
        return (format(start ^ goal,"b")).count("1")
        

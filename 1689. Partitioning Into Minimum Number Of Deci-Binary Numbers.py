class Solution:
    
    def minPartitions(self, n: str) -> int:
        
        a = int(n)
        #print(n)
        count = 0
        digits = [int(x) for x in str(n)]
        return max(digits)
        
        

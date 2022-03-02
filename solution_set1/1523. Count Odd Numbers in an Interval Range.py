##ss
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        ##count of odd numbers
        
        if low%2==0 and high%2==0:
            return (high - low)//2
        
        elif low%2!=0 and high%2==0:
            return 1 + (high-low-1)//2
        
        elif low%2==0 and high%2!=0:
            return 1 + (high-1-low)//2
        
        else:
            return 2 + (high-low-2)//2
        

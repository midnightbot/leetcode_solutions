class Solution:
    def climbStairs(self, n: int) -> int:
        
        temp1 = 1
        temp2 = 2
        ans = 0 
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for x in range(2,n):
            ans=temp1+temp2
            temp1 = temp2
            temp2 = ans
            
        return ans
        

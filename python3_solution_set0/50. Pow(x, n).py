class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0:
            return 0
        elif n == 1:
            return x
        elif x == 1 or n == 0:
            return 1
        
        elif x == -1 and n%2==0:
            return 1
        
        elif x == -1 and n%2!=0:
            return -1
        
        elif n == -1:
            return 1/x
        
        half_ans = self.myPow(x,n//2)
        ans = half_ans * half_ans
        
        if n%2!=0:
            return ans*x
        
        return ans

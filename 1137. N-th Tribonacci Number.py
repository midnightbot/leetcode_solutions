class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        #print(memo)
        
        if n in memo:
            return memo[n]
        if n == 0:
            #memo[0] = 0
            return 0
        
        elif n==1:
            #memo[1] = 1
            return 1
        
        elif n==2:
            #memo[2] = 2
            return 1
        
        elif n>=3:
            memo[n] = (self.tribonacci(n-1,memo)+self.tribonacci(n-2,memo)+self.tribonacci(n-3,memo))
            return memo[n]
        

##ss
class Solution:
    def countOrders(self, n: int) -> int:
        
        ## drop is after pickup

        ## if n = 1 p1 d1 is the only possible combination
        
        ## if n == 2
        ## _ _ _ _
        ## p1 - - d1
        ## p1 - d1 -
        ## p1 d1 - - 
        ## - p1 d1 -
        ## - p1 - d1
        ## - - p1 d1
        ## therefore for every 'n' there will be '2n' slots in total
        ## number of ways to place a single p,d pair
        ##p1 _ _ _ -> 3
        ## - p1 - - -> 2
        ## - - p1 - -> 1
        ## 6 ways
        ## which is equal to sum of integers 1+2+3+..+2n-1 = 2n * (2n-1) / 2 -> sum of 2n-1 consecutive numbers
        ##so total ways all pairs could be placed would be 
        ## 2n * (2n-1)/2 * (number of ways n-1 pairs can be placed)
        ## 2n * (2n-1)/2 * dp[x-1]
        
        ##Solution 1
        ### Time complexity -> O(n) Space Complexity -> O(n)
        """"
        modulo = 10**9 + 7
        dp = [1 for x in range(n+1)]

        for x in range(1,n+1):
            dp[x] = int(((2*x*(2*x-1))/2 * dp[x-1]) % modulo)
            
        return dp[n]
    
        """
        
        ##Solution2
        ###Time Complexity -> O(n), Space Complexity -> O(1)
        modulo = 10**9 + 7
        prev = 1
        for x in range(1,n+1):
            prev = int(((2*x*(2*x-1))/2 * prev) % modulo)
            
        return prev

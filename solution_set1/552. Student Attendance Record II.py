##ss
##Solution 1 (Wrong Answer Attempt1, close to actual answer)
class Solution:
    def checkRecord(self, n: int) -> int:
        
        ## count('A') < 2
        ## never 3 cons L
        
        ## total ways without any condition would be 3**n
        
        ## no-absent 3**n 
        ## 1-absent  n * 3**n-1
        
        ## 4 -> - - - -  more than 2L (l l l l)  -> for pos 0 -> 4 - 0 - 3 + 1
        ##                                       -> for pos 1 -> 4 - 1 - 3 + 1
        ## general formula for 'n' numbers       n - indx - 3 + 1
        
        modulo = 10 ** 9 + 7
        
        reject = 0
        
        
        @lru_cache(None)
        def ways(n):
            if n <= 0:
                return 1
            total1 = (2 ** n ) % modulo
            reject = 0
            for x in range(0,n-3+1):
                reject+= n - x - 3 + 1

                reject = reject % modulo

            total1-=reject
            
            return total1 % modulo
        
        ##case1 no absent
        c1 = ways(n) % modulo
        
        ##case2 1 absent
        c2 = 0
        for x in range(n):
            print(x, n - x - 1)
            c2+= ways(x) * ways(n-x-1)
            
            c2 = c2 % modulo
            #print(c2)
        #print(c1,c2)
        return (c1 + c2)%modulo
        
 ##Solution 2 (Accepted)
 class Solution:
    def checkRecord(self, n: int) -> int:
        
        ## count('A') < 2
        ## never 3 cons L
        
        ## total ways without any condition would be 3**n
        
        ## no-absent 3**n 
        ## 1-absent  n * 3**n-1
        
        ## 4 -> - - - -  more than 2L (l l l l)  -> for pos 0 -> 4 - 0 - 3 + 1
        ##                                       -> for pos 1 -> 4 - 1 - 3 + 1
        ## general formula for 'n' numbers       n - indx - 3 + 1
        
        
        ##end in notL
        ##end in L
        
        ##[n-1] P -> valid
        ##[n-2] PL -> valid
        ##[n-3] PLL -> valid
        ##dp[n] = dp[n-1] + dp[n-2] + dp[n-3]  -> no absent
        
        ##when a single absent
        ##place it at all positions, it will divide string into two parts
        ## if n = 4
        ## A - - - dp[0] * dp[3]
        ## - A - - dp[1] * dp[2]
        ## - - A - dp[2] * dp[1]
        ## - - - A dp[3] * dp[0]
        if n == 1:
            return 3
        elif n == 2:
            return 8
        elif n == 3:
            return 19
        modulo = 10 ** 9 + 7
        dp = [-1 for x in range(n+1)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        
        for x in range(4, len(dp)):
            dp[x] = (dp[x-1] + dp[x-2] + dp[x-3]) % modulo
            
        total = dp[-1] % modulo
        #print(dp)
        for x in range(n):
            total += (dp[x] * dp[n-x-1]) % modulo
            total = total % modulo
            
        return total%modulo
            
        
        
            

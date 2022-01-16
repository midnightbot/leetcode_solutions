##ss
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        ##simple dp
        ##either question is solved or is not solved
        ##if solved dp[x] = points for that question + dp[x+time_cannot_solve]
        ##if not solved dp[x] = dp[x+1]
        dp = [0 for x in range(len(questions))]
        
        dp[-1] = questions[-1][0]
        ans = dp[-1]
        for x in range(len(dp)-2,-1,-1):
            if x + questions[x][1] + 1 < len(questions):
                dp[x] = max(questions[x][0] + dp[x + questions[x][1] + 1] , dp[x+1])
                
            else:
                dp[x] = max(questions[x][0],dp[x+1])
             
            ans = max(ans,dp[x])
        return ans
        

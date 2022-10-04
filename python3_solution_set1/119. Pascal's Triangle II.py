##ss
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ##simple recursion
        dp = [0 for x in range(rowIndex+1)]
        dp[0] = 1
        dp[-1] = 1
        for x in range(1,len(dp)-1):
            dp[x] = self.fill_dp(rowIndex,x)
        
        return (dp)
        
    @lru_cache(None)
    def fill_dp(self,row,col):
        
        if row == 0:
            return 1
        
        elif col==0 or col==row:
            return 1
        
        else:
            return self.fill_dp(row-1,col-1) + self.fill_dp(row-1,col)
        
        
    
        
        

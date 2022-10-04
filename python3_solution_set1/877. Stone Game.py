class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
    
        @lru_cache(None)
        def dp(i,j,player):
            
            if i > j:
                return 0
            
            player = player % 2
            
            if player == 1:
                return max(piles[i] + dp(i+1,j,player+1),piles[j] + dp(i,j-1,player+1))
            
            else:
                return min(-piles[i] + dp(i+1,j,player+1), -piles[j] + dp(i,j-1,player+1))
            
            
        return dp(0,len(piles)-1,0)
            
        

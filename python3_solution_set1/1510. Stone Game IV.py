##ss
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return self.expand(n)
        ##if alice wins then bob should lose
        ##if bob wins alice should lose
        
        ##in any move a player can remove (non zero square number) of stones
        
    @lru_cache(None)   
    def expand(self,n):
        ##if we have n stones left
        ##this player will remove x^2 stones
        ##so try out all the possibility
        ##if removing a particular number of stones make other player to lose, then we win
        ##we have n stones
        ##we remove x^2 stones
        ##n-x^2 stones are left, if the opponent looses with this number of stones, we win
        
        for x in range(1,int(sqrt(n))+1):
            if self.expand(n-x**2) == False:
                return True
            
            
        return False
        

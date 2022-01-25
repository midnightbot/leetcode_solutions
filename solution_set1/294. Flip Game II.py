##ss
class Solution:
    def canWin(self, currentState: str) -> bool:
        
        ##if current player wins, then other player looses and vice verca
        ##try all possible combiations of currentState
        ##if other player loses in any one case, we win
        
        
        def trial(currentState):
            
            for x in range(1,len(currentState)):
                if currentState[x-1] == currentState[x] == '+':
                    temp = currentState[0:x-1] + '--' + currentState[x+1:]
                    if trial(temp) == False:
                        return True
                    
            return False
        
        
        return trial(currentState)
                    
        

##ss
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        result = []
        
        for x in range(1,len(currentState)):
            if currentState[x] == currentState[x-1] == '+':
                temp = currentState[0:x-1] + '--' + currentState[x+1:]
                
                result.append(temp)
        
        return result
        

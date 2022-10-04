##ss
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        maxs = len(words)
        
        for x in range(len(words)):
            maxs = max(maxs, len(words[x]))
            
        for x in range(maxs):
            thisans = ""
            for y in range(len(words)):
                
                if len(words[y]) > x:
                    thisans+=words[y][x]
             
            
            if thisans!=words[x]:
                return False
            
        return True
        

##ss
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        ans = 0
        
        for x in range(len(words)):
            
            if len(words[x]) >= len(pref) and words[x][0:len(pref)] == pref:
                ans+=1
                
        return ans
        

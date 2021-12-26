##ss
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxs = -float('inf')
        
        for x in range(len(sentences)):
            
            maxs = max(maxs, len(sentences[x].split(" ")))
            
        return maxs

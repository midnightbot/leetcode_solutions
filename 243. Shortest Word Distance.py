class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        pos1 = []
        pos2 = []
        
        for x in range(len(wordsDict)):
            if wordsDict[x] == word1:
                pos1.append(x)
                
            elif wordsDict[x] == word2:
                pos2.append(x)
                
        mins = float('inf')
        for x in range(len(pos1)):
            for y in range(len(pos2)):
                if abs(pos1[x]-pos2[y]) < mins:
                    mins = abs(pos1[x]-pos2[y])
                    
        return mins
                
            

        
        
        
        

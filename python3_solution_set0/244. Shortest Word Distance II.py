class WordDistance:
    
    words = {}
    def __init__(self, wordsDict: List[str]):
        global words
        words = {}
        for x in range(len(wordsDict)):
            if wordsDict[x] not in words.keys():
                words[wordsDict[x]] = [x]
                
            else:
                words[wordsDict[x]].append(x)
        
        

    def shortest(self, word1: str, word2: str) -> int:
        
        temp1 = words[word1]
        temp2 = words[word2]
        
        ans = float('inf')
        
        c1 = 0
        c2 = 0
        while c1 < len(temp1) and c2 < len(temp2):
            
            ans = min(ans,abs(temp1[c1] - temp2[c2]))
            
            if temp1[c1] > temp2[c2]:
                c2+=1
                
            else:
                c1+=1
                
        return ans
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

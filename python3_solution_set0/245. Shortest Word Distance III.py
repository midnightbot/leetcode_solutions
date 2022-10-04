##ss
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        if word1 == word2:
            ans = float('inf')
            for x in range(len(wordsDict)):
                if wordsDict[x] == word1:
                    #var = False
                    for y in range(x+1,len(wordsDict)):
                        if wordsDict[y] == word2:
                            #var = True
                            ans = min(ans, y-x)
                            break
                            
            return ans
                            

        dicts = {}
        for x in range(len(wordsDict)):
            if wordsDict[x] == word1 and word1 not in dicts.keys():
                dicts[word1] = [x]
                
            elif wordsDict[x] == word1 and word1 in dicts.keys():
                dicts[word1].append(x)
                
                
            elif wordsDict[x] == word2 and word2 not in dicts.keys():
                dicts[word2] = [x]
                
                
            elif wordsDict[x] == word2 and word2 in dicts.keys():
                dicts[word2].append(x)
                
        comp1 = dicts[word1]
        comp2 = dicts[word2]
        i = 0
        j = 0
        ans = float('inf')
        while i < len(comp1) and j < len(comp2):
            ans = min(ans, abs(comp1[i] - comp2[j]))
            
            if comp1[i] > comp2[j]:##if num1 is greater make num2 big therefore reducing differnece between them
                j+=1
                
            else:
                i+=1
                
        return ans

            
            
        

##ss
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        ans = "" 
        words = sorted(words)
        print(words)
        for x in range(len(words)):
            
            if len(words[x]) > len(ans):
                temp = ""
                var = False
                #print(words[x])
                for y in range(len(words[x])):
                    temp+=words[x][y]
                    if temp not in words:
                        var = True
                        break
                        
                if var == False:
                    ans = words[x]
                    
                    
        return ans
                        
                

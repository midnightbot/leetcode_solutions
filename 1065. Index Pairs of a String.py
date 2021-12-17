##ss
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        ans = []
        for x in range(len(text)):
            for y in range(len(words)):
                var = False
                for z in range(len(words[y])):
                    if x+z >= len(text):
                        var = True
                    elif x+z < len(text) and words[y][z]!=text[x+z]:
                        var = True
                        break
                        
                        
                if var == False:
                    ans.append([x,x+len(words[y])-1])
           
        ans = sorted(ans)
        return ans

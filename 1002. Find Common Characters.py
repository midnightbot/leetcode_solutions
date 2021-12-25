##ss
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        check = [[0 for x in range(len(words))] for y in range(26)]
        
        for x in range(len(words)):
            for y in range(len(words[x])):
                check[ord(words[x][y])-ord('a')][x]+=1
                
        ans = []
        
        for x in range(len(check)):
            mins = min(check[x])
            
            for y in range(mins):
                ans.append(chr(97+x))
                
        return ans

##ss
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        check = text.split(" ")
        
        print(check)
        
        ans = 0
        
        for x in range(len(check)):
            var = False
            for y in range(len(brokenLetters)):
                if brokenLetters[y] in check[x]:
                    var = True
                    break
                    
                    
            if var == False:
                ans+=1
                
        return ans
        

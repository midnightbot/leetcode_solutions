class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        num1 = len(word1)
        num2 = len(word2)
        
        if num1<num2:
            for x in range(num1):
                ans+=word1[x]
                ans+=word2[x]
            for y in range(num1,num2):
                ans+=word2[y]
                
        elif num1==num2:
            for x in range(num1):
                ans+=word1[x]
                ans+=word2[x]
                
        elif num1>num2:
            for x in range(num2):
                ans+=word1[x]
                ans+=word2[x]
            for y in range(num2,num1):
                ans+=word1[y]
                
        return ans
            
        

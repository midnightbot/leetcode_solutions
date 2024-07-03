class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for x in range(26):
            if chr(97+x) in word and chr(65+x) in word:
                ans+=1 
        return ans
        

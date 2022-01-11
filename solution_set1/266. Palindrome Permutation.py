##ss
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        dicts = {}
        for x in range(len(s)):
            if s[x] in dicts:
                dicts[s[x]]+=1
                
            else:
                dicts[s[x]] = 1
                
        odds = 0
        for x in dicts.keys():
            if dicts[x]%2!=0:
                odds+=1
                
        return odds <=1
        

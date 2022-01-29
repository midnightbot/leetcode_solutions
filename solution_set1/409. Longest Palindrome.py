##ss
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dicts = {}
        #return 0
        for x in range(len(s)):
            if s[x] in dicts:
                dicts[s[x]]+=1
                
            else:
                dicts[s[x]] = 1
                
        odd = 0
        full = 0
        for x in dicts:
            #tot+=1
            if dicts[x]%2!=0:
                odd+=1
                
            if dicts[x] >=2:
                full+= dicts[x] // 2
                
        if odd == 0:
            return full*2
        
        elif odd >=1:
            return (full)*2 + 1
        
        

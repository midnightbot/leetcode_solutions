##ss
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        ans = -1
        dicts = {}
        for x in range(len(s)):
            if s[x] in dicts:
                ans = max(ans, x - dicts[s[x]] - 1)
                
            else:
                dicts[s[x]] = x
                
        return ans
        

## Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = []
        
        for x in range(len(s)-1):
            counter = 1
            for y in range(x+1,len(s)):
                if s[y] not in s[x:y]:
                    counter+=1
                    
                else:
                    break
                    
            ans.append(counter)
        if len(s) ==1:
            return 1
        if len(ans) == 0 and len(s)!=0 and s[0] == " ":
            return 1
        
        if len(ans) == 0:
            return 0
        
        else:
            return max(ans)
        
        

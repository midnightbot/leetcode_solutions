##ss
##Solution 1 (Intelligent Brute Force)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""
        lens = len(ans)
        for x in range(len(s)):
            for y in range(len(s)-1,x-1,-1):
                if y-x < lens:
                    break
                if s[x:y+1] == s[x:y+1][::-1]:
                    if len(s[x:y+1]) > lens:
                        ans = s[x:y+1]
                        lens = len(s[x:y+1])
                        break
                        
        return ans
                
        

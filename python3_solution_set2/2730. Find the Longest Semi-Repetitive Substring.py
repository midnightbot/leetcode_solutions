class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ## simple brute force solution
        ## check all substrings if they are semi-repetitive
        ans = 0

        def check(s):
            c = 0
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    c+=1
            
            return c <= 1

        for x in range(len(s)):
            for y in range(x+1, len(s)+1):
                if check(s[x:y]):
                    ans = max(ans, y-x)
        return ans

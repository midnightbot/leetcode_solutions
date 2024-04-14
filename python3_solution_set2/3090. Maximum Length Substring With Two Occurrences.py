class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        def isValid(str):
            temp = Counter([x for x in str])
            return max(temp.values()) <= 2

        ans = 0
        for x in range(len(s)):
            for y in range(x+1, len(s)):
                if isValid(s[x:y+1]):
                    ans = max(ans, y-x+1)
        return ans
        

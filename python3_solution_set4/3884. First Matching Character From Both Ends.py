class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for x in range(n//2 + 1):
            if s[x] == s[n-x-1]:
                return x
        return -1
        

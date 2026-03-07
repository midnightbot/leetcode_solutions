class Solution:
    def largestEven(self, s: str) -> str:
        s = s[::-1]
        n = len(s)
        
        for x in range(n):
            if s[x] == '1':
                continue
            else:
                return s[x:][::-1]
        return ''
        

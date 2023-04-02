class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        def valid(str):

            mids = len(str)//2
            return [x for x in str[:mids]] == ['0' for x in range(mids)] and [x for x in str[mids:]] == ['1' for x in range(mids)] and len(str)%2==0

        lens = 0
        for x in range(len(s)):
            for y in range(x+1,len(s)):
                if valid(s[x:y+1]):
                    lens = max(lens, y-x+1)

        return lens

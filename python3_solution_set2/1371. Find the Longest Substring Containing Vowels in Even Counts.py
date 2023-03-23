class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        maps = {0:-1}
        vals = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}

        curr = 0
        ans = 0
        for x in range(len(s)):
            if s[x] in vals:
                curr^=vals[s[x]]
            if curr not in maps:
                maps[curr] = x
            else:
                ans = max(ans, x- maps[curr])

        return ans

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        ## as soon as value becomes negative start a new string

        val = {}
        for indx, x in enumerate(chars):
            val[x] = vals[indx]



        ans = 0
        for x in range(26):
            if chr(x + ord('a')) not in val:
                val[chr(x + ord('a'))] = x+1

        cost = 0
        for x in range(len(s)):
            if cost + val[s[x]] >= 0:
                cost+=val[s[x]]
                ans = max(ans, cost)

            else:
                cost = 0
        return ans

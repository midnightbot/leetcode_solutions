class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        ans = 0
        for x in range(len(s)):
            for y in range(x+1,len(s)+1):
                curr_s = s[x:y]
                if curr_s.count('1') <= k or curr_s.count('0') <= k:
                    ans+=1

        return ans

        

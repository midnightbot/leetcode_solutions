class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for x in range(len(s)):
            ans+= (x+1) * (ord('z') - ord(s[x]) + 1)
        return ans
        

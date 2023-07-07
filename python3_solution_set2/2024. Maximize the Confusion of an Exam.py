class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:

        ans = 0

        count = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] == 'T':
                count+=1
            
            while count > k:
                if s[l] == 'T':
                    count-=1
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        count = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] == 'F':
                count+=1
            
            while count > k:
                if s[l] == 'F':
                    count-=1
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        return ans

class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        ans = 0

        for x in s:
            if x == 'E':
                count+=1
                ans = max(ans, count)
            else:
                count-=1
        return ans
        

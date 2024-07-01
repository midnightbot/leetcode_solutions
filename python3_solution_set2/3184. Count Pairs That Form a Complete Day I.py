class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0

        for x in range(len(hours)):
            for y in range(x+1, len(hours)):
                if (hours[x]+hours[y])%24==0:
                    ans+=1
        return ans
        

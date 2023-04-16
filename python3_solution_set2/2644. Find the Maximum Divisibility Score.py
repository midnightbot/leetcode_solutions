class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        ans = []

        for d in divisors:
            count = 0
            for it in nums:
                if it%d == 0:
                    count+=1
            ans.append(count)

        
        maxs = max(ans)
        result = float('inf')
        for x in range(len(divisors)):
            if ans[x] == maxs:
                result = min(result, divisors[x])

        return result

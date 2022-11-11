import math
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:

        @lru_cache(None)
        def find_ans(indx):
            if indx == 0:
                return 1
            elif indx < 0:
                return 0
            else:
                ans = float('inf')
                for x in range(0, indx+1):
                    if math.gcd(nums[x], nums[indx]) > 1:
                        ans = min(ans, 1 + find_ans(x-1))

                return ans
        ans = find_ans(len(nums)-1)
        return ans if ans!=float('inf') else -1




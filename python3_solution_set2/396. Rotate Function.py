class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        pre_sum = [nums[0]]
        for x in nums[1:]:
            pre_sum.append(pre_sum[-1] + x)

        def find_first(arr):
            ans = 0
            for x in range(len(arr)):
                ans+= x*arr[x]

            return ans

        def find_anss(nums, r1):
            result = [r1]
            prev_inc = 0
            decrease = 0
            for x in range(len(nums)-1):
                increase = pre_sum[-2-x]
                decrease = nums[-1-x] * (len(nums) - 1)
                result.append(result[-1] + increase - decrease + prev_inc)
                prev_inc+=nums[-1-x]

            return result

        a = find_first(nums)
        anss = find_anss(nums, a)
        #print(anss)
        return max(anss)

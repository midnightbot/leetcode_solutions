class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        temp = accumulate(nums)
        temp = list(temp)
        ans = 0
        n = len(nums)
        for x in range(n-1):
            if nums[x] > (temp[-1] - temp[x])/(n-x-1):
                ans+=1
        return ans
        

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        pre = []
        pre.append(nums[0])
        n = len(nums)
        for x in range(1, len(nums)):
            pre.append(pre[-1] + nums[x])

        ans = []

        for x in range(0, len(nums)):
            if x-k>=0 and x+k<n:
                ans.append((pre[x+k] - pre[x-k] + nums[x-k])//((2*k)+1))
            else:
                ans.append(-1)
        return ans

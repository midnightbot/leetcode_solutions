class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums = [format(x,'b') for x in nums]
        maxs = max([len(z) for z in nums])
        for i in range(len(nums)):
            if len(nums[i]) != maxs:
                diff = maxs - len(nums[i])
                nums[i] = "".join(["0" for f in range(diff)]) + nums[i]

        ans = 0
        nums = [z[::-1] for z in nums]
        for i in range(maxs):
            cnt = 0
            for f in range(len(nums)):
                if nums[f][i] == "1":
                    cnt+=1
            if cnt >= k:
                ans += 2**i
        return ans    

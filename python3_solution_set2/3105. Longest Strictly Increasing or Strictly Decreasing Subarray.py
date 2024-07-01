class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0

        for x in range(len(nums)):
            for y in range(x,len(nums)):
                arr=nums[x:y+1]
                if arr == sorted(arr) and len(set(arr)) == len(arr):
                    ans = max(ans, len(arr))
                elif arr == sorted(arr,reverse=True) and len(set(arr)) == len(arr):
                    ans = max(ans, len(arr))
        return ans
        

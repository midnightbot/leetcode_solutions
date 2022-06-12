##ss
## simple prefix sum
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        pre = [0] + list(accumulate(nums))
        #print(pre)
        if len(nums) == 1:
            return nums[0]
        ans = 0
        seen = {}
        last = 0
        for x in range(len(nums)):
            if nums[x] in seen:## sum from indx to x-1
                indx = seen[nums[x]]
                
                last = max(last, indx)
                
            seen[nums[x]] = x + 1
            ans = max(ans, pre[x+1] - pre[last])
            
        return ans

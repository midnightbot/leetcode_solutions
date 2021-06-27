class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
        temp = int(len(nums)/3)
        nums = sorted(nums)

        for x in range(len(nums) - temp ):
            if nums[x] == nums[x+temp]:
                if nums[x] not in ans:
                    ans.append(nums[x])
                    x = x+ temp
        
                
        return ans
        

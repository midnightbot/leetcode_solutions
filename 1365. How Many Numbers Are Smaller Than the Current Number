class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [""]*len(nums)
        
        for x in range(len(nums)):
            count = 0
            for i in range(len(nums)):
                if i!=x and nums[x]>nums[i]:
                    count +=1 
                ans[x] = count
        return ans
            
        

##ss
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        nums = []
        nums.append(0)
        for x in range(1,len(security)):
            if security[x] <= security[x-1]:
                nums.append(nums[len(nums)-1]+1)
                
            else:
                nums.append(0)
                
                
        #print(nums)
        nums2 = [0 for x in range(len(security))]
        nums2[len(nums2)-1] = 0
        
        for x in range(len(security)-2,-1,-1):
            if security[x] <= security[x+1]:
                nums2[x] = 1 + nums2[x+1]
                
            else:
                nums2[x] = 0
                
        ans = []
        
        for x in range(len(nums)):
            if nums[x] >=time and nums2[x] >=time:
                ans.append(x)
                
        return ans
                
        

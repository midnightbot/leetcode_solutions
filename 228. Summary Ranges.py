class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums)==0:
            return nums
        nums.append(nums[len(nums)-1])

       
        start = nums[0]
        end = nums[0]
        
        
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1] - 1 :
                end = nums[x+1]
                
            else:
                if start==end:
                    ans.append(str(start))
                    start = nums[x+1]
                    end = nums[x+1]
                    
                else:
                    ans.append(""+str(start)+"->"+str(end)+"")
                    start = nums[x+1]
                    end = nums[x+1]
                    
                    
        return ans
            
                
            
        

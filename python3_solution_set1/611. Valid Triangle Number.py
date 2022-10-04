##ss
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        ## a+b > c for all triplest and alla,b,c
        ## naive O(n^3) solution also acc
        nums = sorted(nums)
        
        count = 0
        
        
        for x in range(len(nums)-1,1,-1):
            
            l = 0
            r = x - 1
            
            while l < r:
                if nums[l] + nums[r] > nums[x]:
                    count+= r - l
                    r-=1
                    
                elif nums[l] + nums[r] <= nums[x]:
                    l+=1
                    
        return count
                    
        

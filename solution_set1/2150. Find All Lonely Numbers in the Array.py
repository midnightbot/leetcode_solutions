##ss
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        all_elem = set(nums)
        
        count = {}
        
        for x in range(len(nums)):
            if nums[x] in count:
                count[nums[x]]+=1
                
            else:
                count[nums[x]] = 1
                
        ans = []
        
        for x in count.keys():
            if count[x] == 1 and (x-1) not in all_elem and (x+1) not in all_elem:
                ans.append(x)
                
        return ans
            
        

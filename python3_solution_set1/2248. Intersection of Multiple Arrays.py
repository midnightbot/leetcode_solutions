##ss
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        if len(nums) == 1:
            return sorted(nums[0])
        
        temp = set()
        for x in nums[0]:
            temp.add(x)
            
        def make_set(arr):
            ans = set()
            
            for x in arr:
                ans.add(x)
                
            return ans
        
        for x in range(1,len(nums)):
            #print(x,nums,temp)
            temp = temp.intersection(make_set(nums[x]))
            #print(temp)
            
       # print(temp)
        if temp is None:
            return []
        
        return sorted(list(temp))
            
        

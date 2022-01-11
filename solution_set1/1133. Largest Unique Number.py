##ss
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        dicts = {}
        nums = sorted(nums,reverse = True)
        
        for x in range(len(nums)):
            if nums[x] in dicts:
                dicts[nums[x]]+=1
            else:
                dicts[nums[x]] = 1
                
        for x in dicts.keys():
            if dicts[x] == 1:
                return x
            
        return -1

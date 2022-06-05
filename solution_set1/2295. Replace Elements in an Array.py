class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        pos = {}
        
        for x in range(len(nums)):
            pos[nums[x]] = x
            
        
        for x,y in operations:
            temp = pos[x]
            nums[pos[x]] = y
            pos.pop(x)
            pos[y] = temp
         
        return nums

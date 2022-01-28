##ss
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        ##find longest cycle in the given graph
        
        graphs = []
        maxs = -1
        visited = set()
        thisset = set()
        for x in range(len(nums)):
            
            if nums[x] not in visited:
                thisset = set()
                start = x
                while nums[start] not in thisset:
                    visited.add(nums[start])
                    thisset.add(nums[start])
                    start = nums[start]
                    #visited.add()
                maxs = max(maxs,len(thisset))
                
        return maxs
        
        

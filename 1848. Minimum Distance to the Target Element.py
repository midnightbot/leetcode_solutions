class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        counts = nums.count(target)
        #print(counts)
        if counts ==1:
            return abs(nums.index(target) - start)
        
        else:
            ans = []
            for x in range(len(nums)):
                if nums[x]==target:
                    temp = abs(x - start)
                    ans.append(temp)
                    
            return min(ans)
        

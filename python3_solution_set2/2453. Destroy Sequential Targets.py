class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        og_nums = nums
        nums = [x%space for x in nums]
        
        temp = Counter(nums)
        
        c = -1
        ans = []
        for x in temp:
            if temp[x] > c:
                ans = [x]
                c = temp[x]
                
            elif temp[x] == c:
                ans.append(x)
                
        result = float('inf')
        
        seen = set(ans)
        for x in range(len(nums)):
            if nums[x] in seen:
                result = min(result, og_nums[x])
                
        return result
            

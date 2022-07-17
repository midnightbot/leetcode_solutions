##ss
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        maps = {}
        ans = -1
        
        for x in nums:
            dsum = sum([int(f) for f in str(x)])
            if dsum in maps:
                maps[dsum].append(x)
            else:
                maps[dsum] = [x]
                
       
       
        for x in maps:
            if len(maps[x])>=2:
                maps[x] = sorted(maps[x])
                ans = max(ans, maps[x][-1]+maps[x][-2])
        return ans

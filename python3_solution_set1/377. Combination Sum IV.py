##ss
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        self.ways = 0
        
        @lru_cache(None)
        def make_sum(remaining):
            
            if remaining == 0:
                return 1
            
            elif remaining < 0:
                return 
            
            else:
                ans = 0
                for x in range(len(nums)):
                    if remaining - nums[x] >=0:
                        ans+=make_sum(remaining-nums[x])
                        
                return ans
                
        return make_sum(target)

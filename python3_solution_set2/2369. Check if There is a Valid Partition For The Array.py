##ss
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @lru_cache(None)
        def find_ans(indx):
            if indx >= n:
                return True
            
            else:
                ans = False
                if indx + 1 < n:
                    if nums[indx] == nums[indx+1]:
                        ans = ans or find_ans(indx+2)
                
                if indx + 2 < n:
                    if nums[indx] == nums[indx+1] == nums[indx+2]:
                        ans = ans or find_ans(indx+3)
                        
                    if nums[indx]+2 == nums[indx+1]+1 == nums[indx+2]:
                        ans = ans or find_ans(indx+3)
                        
                return ans
            
        return find_ans(0)

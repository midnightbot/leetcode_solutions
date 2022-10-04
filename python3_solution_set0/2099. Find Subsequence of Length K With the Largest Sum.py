##ss
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        ##each element will either be considered or not considered
        ##basically find largest k elements and return ans
        ##can also used heap to make it asymptotically faster
        ans = []
        
        for x in range(len(nums)):
            if len(ans) < k:
                ans.append(nums[x])
                
            else:
                if min(ans) < nums[x]:
                    ans.append(nums[x])
                    ans.remove(min(ans))
                    
        return ans
        

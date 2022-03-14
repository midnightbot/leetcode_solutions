##ss
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        ##will be a line or no line
        ##dp[i][j] -> max lines of nums[i:] and nums[j:]
        
        @lru_cache(None)
        def ways(i,j):
            #print(i,j)
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            else:
                
                ans1 = 0
                ans2 = 0
                if nums1[i] in nums2[j:]:##match ('ith' char of nums1 matches to some char in nums2)
                    ans1 = 1 + ways(i+1, j + nums2[j:].index(nums1[i]) + 1)
                
                
                ##no match
                ans2 = ways(i+1,j)
                    
                    
                return max(ans1,ans2)
            
        return ways(0,0)

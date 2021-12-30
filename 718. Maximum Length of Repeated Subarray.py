##ss
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        ##dp[i][j] be max length of subarray that is same in nums1 [0..i] and nums2[0..j]
        
        
        
        dp = [[0 for x in range(len(nums1)+1)] for y in range(len(nums2)+1)]
        
        
        #self.print_dp(dp)
        for x in range(1,len(dp)):
            for y in range(1,len(dp[0])):
                if nums2[x-1] == nums1[y-1]:
                    dp[x][y] = 1 + dp[x-1][y-1]
                    
                #else:
                    #dp[x][y] = max(dp[x][y-1],dp[x-1][y])
                    
                    
        #self.find_max(dp)
        #return max(dp)
        #return dp[len(nums1)][len(nums2)]
        return self.find_max(dp)
    def find_max(self,dp):
        
        maxs = 0
        
        for x in range(len(dp)):
            maxs = max(maxs, max(dp[x]))
            
        return maxs

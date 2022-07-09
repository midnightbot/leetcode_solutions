## Solution 1 - TLE
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        ## return max score
        
        @cache
        def find_ans(indx):
            if indx <= 0:
                return nums[0]
            
            else:
                ans = -float('inf')
                for x in range(1,k+1):
                    ans = max(ans, find_ans(indx-x))
                    
                return ans + nums[indx]
            
        return find_ans(len(nums)-1)
        
## Solution2 - Accepted
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        ## return max score
        n = len(nums)
        dp = [0 for x in range(n)]
        
        dp[0] = nums[0]
        q = []
        
        heapq.heappush(q,(-nums[0],0))
        
        for x in range(1,n):
            
            while q[0][1] < x - k:
                heapq.heappop(q)
                
            dp[x] = nums[x] + dp[q[0][1]]
            heapq.heappush(q,(-dp[x],x))
            
        return dp[-1]

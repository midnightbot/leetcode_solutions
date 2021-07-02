class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        
        nums = sorted(nums)
        k = int(len(nums)/2 - 1)
        #print(k)
        ans = []
        for x in range(k+1):
            temp = nums[x] + nums[len(nums)-1-x]
            ans.append(temp)
            
        return max(ans)
            
        

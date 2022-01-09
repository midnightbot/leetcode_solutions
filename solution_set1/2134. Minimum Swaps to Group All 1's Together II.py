##ss
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = nums.count(1)
        circ = nums + nums + nums
        
        
        #print(circ)
        zeros = circ[len(nums):len(nums)+ones].count(0)
        ans = zeros
        for x in range(len(nums),len(circ)-ones-1):
            #print(x,x+ones)
            if circ[x] == 0 and circ[x+ones] == 1:
                zeros-=1
                ans = min(ans,zeros)
                
            elif circ[x] == 0 and circ[x+ones] == 0:
                ans = min(ans,zeros)
                
            elif circ[x] == 1 and circ[x+ones] == 1:
                ans = min(ans,zeros)
                
                
            elif circ[x] == 1 and circ[x+ones] == 0:
                zeros+=1
                ans = min(ans,zeros)
                
        return ans
        

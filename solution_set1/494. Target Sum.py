##ss
##simple recursion with memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #print(pow(2,20))
        memo = {}
        self.result = 0
        self.expand(nums,0,target,memo)
        return memo[(0,target)]
    
    def expand(self,nums,pointer,target,memo):
        #print(pointer,target)
        if pointer == len(nums):
            if target == 0:
                return 1
            else:
                return 0
               
        elif (pointer,target) in memo:
            return memo[(pointer,target)]
        
        elif pointer < len(nums):
            
            a = self.expand(nums,pointer+1,target + nums[pointer],memo)
            b = self.expand(nums,pointer+1,target - nums[pointer],memo)
            #print(pointer,target)
            memo[(pointer,target)] = a+b
            return memo[(pointer,target)]
        
        

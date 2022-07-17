##ss
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        if len(numsDivide) == 1:
            nums = sorted(nums)
            for x in range(len(nums)):
                if numsDivide[0]%nums[x]==0:
                    return x
            return -1
        
        
        
        if len(numsDivide)>=2:
            dels =0
            t = gcd(numsDivide[0],numsDivide[1])
            #print(t)
            for x in range(2,len(numsDivide)):
                t = gcd(t,numsDivide[x])

            #print(t)

            nums = sorted(nums)
            for x in range(len(nums)):
                if t%nums[x] == 0:
                    return x

            return -1
        

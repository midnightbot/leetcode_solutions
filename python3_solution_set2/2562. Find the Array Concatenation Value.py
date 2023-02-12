class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        if len(nums)%2==0:
            temp = [int(str(nums[x])+str(nums[-x-1])) for x in range(len(nums)//2)]

        else:
            temp = [int(str(nums[x])+str(nums[-x-1])) for x in range(len(nums)//2)] + [nums[len(nums)//2]]

        #ans = 0
        #print(temp)
        return sum(temp)

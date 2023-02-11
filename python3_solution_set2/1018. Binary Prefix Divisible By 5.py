class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        num = 1 if nums[0]==1 else 0
        ans = []
        
        ans.append(num%5==0)

        for x in range(1,len(nums)):
            num = num << 1
            num+= 1 if nums[x] ==1 else 0
            #print(num)
            ans.append(num%5==0)

        return ans

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        

        nums = nums[::-1]
        prev = nums[-1] + nums[-2]
        count = 0
        while len(nums) >= 2:
            num1,num2 = nums.pop(), nums.pop()
            # print(num1,num2,prev)
            if num1+num2 == prev:
                count+=1
            else:
                return count

        return count
        

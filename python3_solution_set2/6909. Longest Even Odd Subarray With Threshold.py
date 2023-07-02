class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0

        for x in range(len(nums)):
            for y in range(x, len(nums)):
                temp = nums[x:y+1]
                
                satisfy  = True
                ## condition1
                if temp[0]%2!=0:
                    satisfy = False
                    break

                ##condition2
                for it in range(x, y):
                    if nums[it]%2 == nums[it+1]%2:
                        satisfy = False
                        break
                
                ##condition3
                for it in range(x, y+1):
                    if nums[it] > threshold:
                        satisfy = False
                        break
                

                if satisfy == True:
                    ans = max(ans, y-x+1)



        return ans

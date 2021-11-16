## Solution 1 (Space O(1))
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        counter = 0
        
        while counter<k:
            counter+=1
            temp = nums.pop(len(nums)-1)
            nums.insert(0,temp)
            
        #print(nums)
        
 ########################################################################################    
## Solution 2 (Space Complexity : O(n))

class Solution: ()
    def rotate(self, nums: List[int], k: int) -> None:
        
        counter = 0
        temp1 = nums[(len(nums)-k)%len(nums):len(nums)]
        temp2 = nums[0:(len(nums)-k)%len(nums)]
        temp = temp1 + temp2
        for x in range(len(temp)):
            nums[x] = temp[x]
########################################################################################
## Solution 3 (Almost same as Solution 1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        counter = 0
        
        while counter<(k%len(nums)):
            counter+=1
            temp = nums.pop(len(nums)-1)
            nums.insert(0,temp)
            
        #print(nums)
        

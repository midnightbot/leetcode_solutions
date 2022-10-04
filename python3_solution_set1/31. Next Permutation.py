##ss
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##next permutation (circular pattern)
        
        ##step1 : find 1st decreasing elem
        ##step2 : from there find the smallest largest number from elem  in nums[x:]
        ##step3: rev nums[x:]
        
        if sorted(nums,reverse = True) == nums:
            #print("inside",nums)
            temp = copy.deepcopy(nums)
            temp = temp[::-1]
            #print(temp,nums)
            for x in range(len(nums)):
                nums[x] = temp[x]
            
        else:
            for x in range(len(nums)-2,-1,-1):
                if nums[x] < nums[x+1]:

                    #print(x)
                    mins = float('inf')
                    pos = -1
                    for z in range(x,len(nums)):
                        if nums[z] > nums[x] and nums[z] <= mins:
                            if mins >= nums[z]:
                                mins = nums[z]
                                pos = z
                    print(pos)
                    if pos!=-1:
                        nums[x], nums[pos] = nums[pos],nums[x]
                        #print(nums,"before")
                        for z in range((len(nums)-x-1)//2):
                            nums[z+x+1],nums[-1-z] = nums[-1-z],nums[z+x+1]
                        #print(nums)
                        #nums = nums[0:x+1] + nums[x+1:][::-1]
                        #print(nums,"after")
                        break
                    
      
        

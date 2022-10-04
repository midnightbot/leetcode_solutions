##sss
##see Q31 for help
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        
        #swaps = 0
        ##step1 : find the kth smallest wonderful number
        ##step2 : find number of swaps
        
        nums = [int(x) for x in num]
        og_nums = copy.deepcopy(nums)
        swaps = 0
        def nextperm(nums): ## see leetcode Q31 Next permutation
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
                    #print(pos)
                    if pos!=-1:
                        nums[x], nums[pos] = nums[pos],nums[x]
                        #print(nums,"before")
                        for z in range((len(nums)-x-1)//2):
                            nums[z+x+1],nums[-1-z] = nums[-1-z],nums[z+x+1]
                        #print(nums)
                        #nums = nums[0:x+1] + nums[x+1:][::-1]
                        #print(nums,"after")
                        break
            
        for x in range(k):
            nextperm(nums)
            
        ## now we have done 'k' permutations
        
        #print(nums,og_nums)
        ##now starting step2, to find min adjacent swaps
        
        for x in range(len(nums)):
            if nums[x] == og_nums[x]:
                continue
                
            for y in range(x,len(nums)):
                if og_nums[y] == nums[x]:
                    swaps+= y - x
                    
                    og_nums = og_nums[:x] + [og_nums[y]] + [og_nums[z] for z in range(x, len(num)) if z!=y]
                    break
                    
        return swaps
                    

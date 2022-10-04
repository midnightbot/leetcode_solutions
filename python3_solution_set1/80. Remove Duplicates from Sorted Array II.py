##ss
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prevs = [nums[0],1]
        remove = 0
        for x in range(1,len(nums)):
            
            if nums[x] == prevs[0] and prevs[1] == 1:
                prevs[1]+=1
                
            elif nums[x] == prevs[0] and prevs[1] >=2:
                remove+=1
                nums[x] = float('inf')
                
                
            elif nums[x]!=prevs[0]:
                prevs = [nums[x],1]
                
                
        #print(nums)
            
        #nums = sorted(nums)
        nums.sort()
        for x in range(remove):
            nums.pop(-1)
            
        print(nums)

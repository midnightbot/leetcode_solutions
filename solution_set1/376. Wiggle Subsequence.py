##ss
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        ##sequence will either end with pos diff or neg diff
        
        ## if it ends in pos diff at index 'x'
        ## len(sequence) = 1 + neg_seq(x-1)
        
        ## if it ends in neg diff at index 'x'
        ## len(seq) = 1 + pos_seq(x-1)
        
        if len(nums) < 2:
            return len(nums)
        
        pos = [1 for x in range(len(nums))]
        neg = [1 for x in range(len(nums))]
        
        for x in range(1,len(nums)):
            
            if nums[x] > nums[x-1]:
                pos[x] = neg[x-1] + 1
                neg[x] = neg[x-1]
                
            elif nums[x] < nums[x-1]:
                neg[x] = pos[x-1] + 1
                pos[x] = pos[x-1]
                
            else:
                neg[x] = neg[x-1]
                pos[x] = pos[x-1]
                
        return max(pos[-1],neg[-1])
        
        
        
        

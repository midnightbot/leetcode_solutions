##ss
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        #print(nums)
        for x in range(len(nums)):
            nums[x] = [self.make_map(nums[x],mapping),nums[x]]
            
        #print(nums)
        
        nums = sorted(nums, reverse = False, key = lambda x:x[0])
        nums = [nums[x][1] for x in range(len(nums))]
        
        return nums
        
    def make_map(self,nums,mapping):
        
        ans = ""
        number = str(copy.deepcopy(nums))
        #number = str(number)
        for x in range(len(number)):
            ans+=str(mapping[int(number[x])])
        
        #print(ans)
        
        return int(ans)

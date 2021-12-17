##ss
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        
        for x in range(len(nums)):
            if nums[x]%2==0:
                even.append(nums[x])
                
            else:
                odd.append(nums[x])
                
        i = 0
        j = 0
        
        for x in range(len(nums)):
            if x%2==0:
                nums[x] = even[i]
                i+=1
                
            else:
                nums[x] = odd[j]
                j+=1
                
        return nums
        

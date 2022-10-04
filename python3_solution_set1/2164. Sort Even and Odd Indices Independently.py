##ss
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        e = []
        o = []
        
        for x in range(len(nums)):
            if x%2==0:
                e.append(nums[x])
                
            else:
                o.append(nums[x])
                
                
        e = sorted(e)
        o = sorted(o)
        o = o[::-1]
        nums = []
        for x in range(min(len(e),len(o))):
            nums.append(e[x])
            nums.append(o[x])
            
        if len(e) > len(o):
            nums.append(e[-1])
        
        elif len(o) > len(e):
        
            nums.append(o[-1])
            
        return nums
        

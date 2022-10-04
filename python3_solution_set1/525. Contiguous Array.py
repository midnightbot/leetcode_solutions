##ss
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dicts = {}
        dicts[0] = -1
        sums = 0
        ans = 0
        for x in range(len(nums)):
            
            if nums[x] == 1:
                sums+=1
            else:
                sums-=1
            #print(sums,0 in dicts)    
            if sums in dicts.keys():
                ans = max(ans,x-dicts[sums])
            else:
                dicts[sums] = x
                
        return ans
        

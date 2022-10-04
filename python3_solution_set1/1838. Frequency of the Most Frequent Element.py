##ss
import bisect
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        fmaps = {}
        
        
        
        prefix = [nums[0]]
        for x in range(1,len(nums)):
            prefix.append(nums[x] + prefix[-1])
        
        prefix.insert(0,0)
        
        fmaps[nums[0]] = 1
        
        for x in range(1,len(nums)):
            
            
            if nums[x] in fmaps:
                fmaps[nums[x]]+=1
                
            else:
                l = 0
                r = x
                temp = x
                while l <= r:
                    mid = (l+r) // 2
                    #print(mid+1,x)
                    if prefix[x]-prefix[mid] + k >= (x-mid)*nums[x]:
                        temp = mid
                        r = mid - 1
                        
                    else:
                        l = mid + 1
                        
                #print(x-temp+1) 
                fmaps[nums[x]] = x - temp + 1
                #print(x-temp + 1)
                
        return max(fmaps.values())   
        
        
        
        
        
        

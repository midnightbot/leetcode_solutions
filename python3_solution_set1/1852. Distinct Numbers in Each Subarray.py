##ss
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        ##ans[i] = ##nums[i:i+k-1]
        ans = [0 for x in range(len(nums)-k+1)]
        #print(ans)
        
        maps = {}
        size = 0
        
        for x in range(k):
            if nums[x] in maps:
                maps[nums[x]]+=1
                
            else:
                size+=1
                maps[nums[x]] = 1
                
                
        ans[0] = size
        
        for x in range(1,len(nums)-k+1,1):
            maps[nums[x-1]]-=1
            
            if maps[nums[x-1]] == 0:
                maps.pop(nums[x-1])
                size-=1
                
            if nums[k+x-1] in maps:
                maps[nums[k+x-1]]+=1
                
            else:
                maps[nums[k+x-1]] = 1
                size+=1
                
            ans[x] = size
            
            
        
        
        return ans

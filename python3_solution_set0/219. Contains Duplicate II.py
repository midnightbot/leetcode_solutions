##ss
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dicts = {}
        
        for x in range(len(nums)):
            if nums[x] not in dicts:
                dicts[nums[x]] = [x]
                
            else:
                dicts[nums[x]].append(x)
                
                
        for x in dicts.keys():
            for i in range(len(dicts[x])-1):
                for j in range(i+1,len(dicts[x])):
                    if dicts[x][j] - dicts[x][i] <=k:
                        return True
                    
                    else:
                        break
                        
        return False
                
        

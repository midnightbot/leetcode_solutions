##ss
from math import comb
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        dicts = {}
        
        for x in range(len(nums)):
            if nums[x] not in dicts:
                dicts[nums[x]] = 1
                
            else:
                dicts[nums[x]]+=1
                
        count = 0
        #print(dicts)
        for x in dicts:
            
            if x==target[0:len(x)] and len(target) > len(x):
                s1 = target[len(x):]
                #s2 = target[len(target)-len(x):]
                if s1 in dicts:
                    if s1!=x:
                        count+=dicts[s1]*dicts[x]
                        
                    else:
                        count+=(dicts[s1]*(dicts[s1]-1))
                        
            #print(count)
        return count
                        
            
        

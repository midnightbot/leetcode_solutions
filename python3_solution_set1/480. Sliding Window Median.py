##ss
import collections
from sortedcontainers import SortedDict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
    
        ans = []
        d = SortedDict()
        for x in range(k):
            if nums[x] in d:
                d[nums[x]]+=1
            else:
                d[nums[x]]=1
                
        #print(d)
                
        ans.append(self.find_median(d,k))
        
        for x in range(1,len(nums)-k+1):
            #print(nums[x-1],"an")
            d[nums[x-1]]-=1
            
            if d[nums[x-1]] == 0:
                d.pop(nums[x-1])
                
            if nums[x+k-1] in d:
                d[nums[x+k-1]]+=1
            else:
                d[nums[x+k-1]] = 1
            ans.append(self.find_median(d,k))
            
        return ans
    def find_median(self,dicts,k):
        #print(k)
        if k%2!=0:
            
            ans = 0
            
            for x in dicts:
                ans+=dicts[x]
                
                if ans >= (k-1)//2 + 1:
                    return x
                
        else:
            ans = 0
            done1 = False
            done2 = False
            #print("ins")
            mids = []
            for x in dicts:
                
                ans+=dicts[x]
                
                if ans >= k//2 and done1 == False:
                    mids.append(x)
                    done1 = True
                    
                if ans >= k//2 + 1 and done2 == False:
                    mids.append(x)
                    done2 = True
                #print(mids)   
                if done1 and done2:
                    return sum(mids) / 2
                
        

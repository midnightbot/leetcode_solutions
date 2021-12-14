##easy
##simple recursion
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        strs = []
        self.combine(candidates,0,target,ans,strs)
        return ans
    
    def combine(self,candidates,i,target,ans,strs):
        #print(strs)
        if i == len(candidates)or sum(strs) == target:
            if sum(strs) == target:
                ans.add(tuple((strs)))
                
        elif sum(strs) < target:
            new_arr = copy.copy(strs)
            new_arr.append(candidates[i])
            self.combine(candidates,i,target,ans,new_arr)
            self.combine(candidates,i+1,target,ans,new_arr)
            self.combine(candidates,i+1,target,ans,strs)
        

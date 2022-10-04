##ss
##Solution 1 (Time Limit Exceeded  172/175 Test cases passed)
##Naive recursion
##Same as Q 39
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        strs = []
        candidates = sorted(candidates)
        self.combine(candidates,0,target,ans,strs)
        return ans
    
    def combine(self,candidates,i,target,ans,strs):
        #print(strs,i)
        
        if target == 0:
            ans.add(tuple(strs))
        elif i > len(candidates)-1:
            return 
     
        elif target < 0:
            return 
  
        elif target > 0:
            
            strs.append(candidates[i])
            if sum(candidates[i+1:len(candidates)]) >= target-candidates[i]:
                self.combine(candidates,i+1,target-candidates[i],ans,strs)
            
                
            strs.pop(len(strs)-1)
            
            if sum(candidates[i+1:len(candidates)]) >= target:
                self.combine(candidates,i+1,target,ans,strs)
            
            
##Solution 2
##2 branches will be
##having atleast 1 of that number
##having no inclusion of that number
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        strs = []
        candidates = sorted(candidates)
        self.combine(candidates,0,target,ans,strs)
        return ans
    
    def combine(self,candidates,i,target,ans,strs):
        #print(strs,i)
        
        if target == 0:
            ans.add(tuple(strs))
            
        elif target < 0:
            return
        
            
        elif i > len(candidates)-1:
            return 
     
        elif target < 0:
            return 
  
        elif target > 0:
            
            strs.append(candidates[i])
            if sum(candidates[i+1:len(candidates)]) >= target-candidates[i]:
                self.combine(candidates,i+1,target-candidates[i],ans,strs)
            
                
            strs.pop(len(strs)-1)
            temp = candidates[i+1:len(candidates)].count(candidates[i])
            if sum(candidates[i+1+temp:len(candidates)]) >= target:
                self.combine(candidates,i+1+temp,target,ans,strs)
            
            
        
        
        

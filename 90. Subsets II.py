##ss
import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        check = []
        self.create(nums,0,ans,[],check)
        #print(len(ans))
        return ans
        
        
    def create(self,nums,i,ans,tset,check):
        
        if len(nums) == 0 or i > len(nums) -1:
            if self.mask(tset) not in check: ##check if no combination of this set is already present in the ans
                ans.add(tuple((tset)))
                check.append(self.mask(tset))
            
        else:
            new_set = copy.deepcopy(tset)
            if new_set == None:
                new_set = [nums[i]]
                
            else:
                new_set.append(nums[i])
            #new_set = new_set.append(nums[i])
            
            self.create(nums,i+1,ans,new_set,check)
            self.create(nums,i+1,ans,tset,check)
            self.create([],i+1,ans,new_set,check)
            
        
    def mask(self,arr): ## create freq map of every answer, so that no combination of this is added again in ans
        ##eg if [1,2,1] in answer then we have to avoid [1,1,2]
        dicts = {}
        arr = sorted(arr)
        for x in range(len(arr)):
            if arr[x] not in dicts.keys():
                dicts[arr[x]] = 1
                
            else:
                dicts[arr[x]]+=1
                
        return dicts
            
            
        

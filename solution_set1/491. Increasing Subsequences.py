##ss
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ##simple recursion
        ##just consider all possible combinations
        
        self.ans = set()
        self.make_sets(nums,0,[])
        return (self.ans)
        
    def make_sets(self,nums,pointer,temp):
        #print(nums,pointer,temp)
        if pointer == len(nums) and len(temp)>=2:
            self.ans.add(tuple(sorted(temp)))
        if len(temp) ==0 and pointer < len(nums):
            newtemp = copy.deepcopy(temp)
            
            newtemp.append(nums[pointer])
            
            self.make_sets(nums,pointer+1,newtemp)
            self.make_sets(nums,pointer+1,temp)
            
        elif pointer < len(nums):
            
            if temp[-1] <= nums[pointer]:
                newtemp = copy.deepcopy(temp)
                newtemp.append(nums[pointer])

                self.make_sets(nums,pointer+1,newtemp)
                self.make_sets(nums,pointer+1,temp)
                
            else:
                self.make_sets(nums,pointer+1,temp)
        

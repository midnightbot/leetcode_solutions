##ss
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = set()

            
        nums = sorted(nums)
        #print(nums)
        
        for x in range(len(nums)-2):
            for y in range(x+1,len(nums)-2):
                
                made = nums[x] + nums[y]
                thisans = self.twosum(nums,y+1,len(nums)-1,target-made)
                
                if thisans!=[]:
                    #print(thisans)
                    #print(x,y)
                    for z in range(len(thisans)):
                        t = thisans[z]+[nums[x],nums[y]]
                        t = sorted(t)
                        #print(t)
                        ans.add(tuple(t))
                    #ans.append([nums[x],nums[y]]+thisans)
                    
        return ans

    def twosum(self,nums,start,end,target):
        choice = []
        while start < end:
            if nums[start] + nums[end] == target:
                choice.append([nums[start],nums[end]])
                #return [nums[start],nums[end]],start,end
                start+=1
                end-=1
            
            
            
            elif nums[start]+ nums[end] < target:
                start+=1
                
            else:
                end-=1
                
        return choice
    
    
    
        

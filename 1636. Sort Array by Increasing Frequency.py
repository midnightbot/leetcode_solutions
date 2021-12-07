class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        dicts = {}
        
        for x in range(len(nums)):
            if nums[x] not in dicts.keys():
                dicts[nums[x]] = 1
                
            else:
                dicts[nums[x]]+=1
             
        queue = []
        for key in dicts.keys():
            queue.append((dicts[key],key))
            
        queue = sorted(queue, key = lambda x : (x[0],-x[1]))
        #queue = sorted(queue, key = lambda x: x[1])
        ans = []
        for x in range(len(queue)):
            for m in range(queue[x][0]):
                ans.append(queue[x][1])
                
        return ans
        

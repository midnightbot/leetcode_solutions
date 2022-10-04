##ss
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ##solution1 : sort and then check O(nlogn)
        ##solution2 : think something about union find
        #print(sorted(nums))
        ##2,3,4,5
        if len(nums) == 0:
            return 0
        parent = [-1 for x in range(len(nums))]
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        
        def union(x,y):
            
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                if xs>ys:
                    parent[xs] = ys
                else:
                    parent[ys] = xs
                
        
        seen = {}
        for x in range(len(nums)):
            
            var = 0
            if nums[x]+1 in seen and nums[x] not in seen:
                union(x,seen[nums[x]+1])
                var+=1
            if nums[x]-1 in seen and nums[x] not in seen:
                union(x,seen[nums[x]-1])
                var+=1
                
            if var == 2:
                #print("insidee",nums[x])
                union(seen[nums[x]+1],seen[nums[x]-1])
            
                
            if nums[x] not in seen:
                seen[nums[x]] = x
          
        
        #print(nums)
        for x in range(len(parent)):
            if parent[x]!=-1:
                parent[x] = find_parent(x)
                
        #print(parent)
        freq = {}
        for x in range(len(parent)):
            if parent[x]!=-1:
                if parent[x] in freq:
                    freq[parent[x]]+=1
                    
                else:
                    freq[parent[x]] = 1
                    
        maxs = 1
        #print(freq)
        for x in freq:
            maxs = max(maxs, 1 +freq[x])
            
        return maxs
        
        

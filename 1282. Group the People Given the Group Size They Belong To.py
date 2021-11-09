class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        nums = 0
        dicts = [[] for x in range(max(groupSizes)+1)]
        #print(dicts)
        for x in range(len(groupSizes)):
            dicts[groupSizes[x]].append(x)
            
        print(dicts)
        ans = []
        for x in range(1,len(dicts)):
            temp = []
            for y in range(0,len(dicts[x]),x):
                temp = []
                for z in range(x):
                    temp.append(dicts[x][y+z])
                
                
                ans.append(temp)
            
        return ans
            
            
            
        

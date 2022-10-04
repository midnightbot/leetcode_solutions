##ss

##Solution 1 (Time Limit Exceeded)
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        dicts = {}
        
        for x in range(len(arr)):
            if arr[x] not in dicts.keys():
                dicts[arr[x]] = [x]
                
            else:
                dicts[arr[x]].append(x)
                
        #print(dicts)
        
        ans = [0 for x in range(len(arr))]
        
        for x in dicts.keys():
            before= 0
            after = 0
            
            for y in range(1,len(dicts[x])):
                after+= abs(dicts[x][y] - dicts[x][0])
                
            #print(dicts[x][0])
            ans[dicts[x][0]] = after
            
            for y in range(1,len(dicts[x])):
                #print(before)
                before+= (abs(dicts[x][y] - dicts[x][y-1])) * y
                #print(before,dicts[x][y] - dicts[x][y-1])
                #after -= abs(dicts[x][y] - dicts[x][y-1]) * (len(dicts[x])-y)
                after = 0
                for z in range(y,len(dicts[x])): ## how can i reduce this loop
                    after+= abs(dicts[x][y] - dicts[x][z])
                    
                #print(before,after)
                ans[dicts[x][y]] = before + after
                
                
        return ans
      
      
      
  ##Solution 2 (Reducing Calculation of after)
  class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        dicts = {}
        
        for x in range(len(arr)):
            if arr[x] not in dicts.keys():
                dicts[arr[x]] = [x]
                
            else:
                dicts[arr[x]].append(x)
                
        #print(dicts)
        
        ans = [0 for x in range(len(arr))]
        
        for x in dicts.keys():
            before= 0
            after = 0
            
            for y in range(1,len(dicts[x])):
                after+= abs(dicts[x][y] - dicts[x][0])
                
            #print(dicts[x][0])
            ans[dicts[x][0]] = after
            
            for y in range(1,len(dicts[x])):
                #print(before)
                before+= (abs(dicts[x][y] - dicts[x][y-1])) * y
                #print(before,dicts[x][y] - dicts[x][y-1])
                after -= abs(dicts[x][y] - dicts[x][y-1]) * (len(dicts[x])-y)
                #for z in range(y,len(dicts[x])): ## how can i reduce this loop
                    #after+= abs(dicts[x][y] - dicts[x][z])
                    
                #print(before,after)
                ans[dicts[x][y]] = before + after
                
                
        return ans
                
                

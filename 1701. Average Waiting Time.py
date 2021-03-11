class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        ans = 0
        currenttime = customers[0][0]
        for x in range(len(customers)):
            
            if currenttime > customers[x][0]:
                ans+= currenttime - customers[x][0] + customers[x][1]
                currenttime = currenttime + customers[x][1]
                
            else:
                ans+= customers[x][1]
                currenttime = customers[x][0] + customers[x][1]
        
        #print(ans)
        return (ans/len(customers))
            
            
            
        

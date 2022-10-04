class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dicts = {}
        ans  = []
        for x in range(len(list1)):
            temp = []
            temp.append(x)
            
            if list1[x] in list2:
                indx = list2.index(list1[x])
                temp.append(indx)
                
            dicts[list1[x]] = temp
         
        ans = float('inf')
        rets  = []
        for x in dicts.keys():
            temp = dicts[x]
            if len(temp) == 2:
                if ans>=temp[0]+temp[1]:
                    ans = temp[0]+temp[1]
                    rets.append((ans,x))
                    
        rets = sorted(rets)
  
        mins = rets[0][0]
        finals = []
        for x in range(len(rets)):
            if rets[x][0] == mins:
                finals.append(rets[x][1])
                
        return finals
                    
                
        
                
        

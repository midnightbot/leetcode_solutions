##ss
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        indx = {}
        result = 0
        #thisans = 0
        left = 0
        for x in range(len(fruits)):
            #print(result,indx)
            if (len(indx.keys()) < 2) or (len(indx.keys())== 2 and fruits[x] in indx):
                indx[fruits[x]] = x
                
            elif len(indx.keys())==2 and fruits[x] not in indx:
                #print('inside')
                temp = self.findmins(indx)
                #print(x,left,"changing")
                result = max(result,x-left)
                left = indx[temp]+1
                indx.pop(temp)
                indx[fruits[x]] = x
                
        #print(result) 
        result = max(result,x-left+1)
        return result
                
    def findmins(self,indx):
        
        if indx[list(indx.keys())[0]] > indx[list(indx.keys())[1]]:
            return list(indx.keys())[1]
        
        else:
            return list(indx.keys())[0]
            
                
        
        
        
        
        
        
        

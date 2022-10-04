##ss
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        count = 0
        
        i = 0
        j = 0
        rounds = 0
        while j < len(target):
            
            if i < len(source) and source[i] == target[j]:
                i+=1
                j+=1
                rounds = 0
                
            elif i < len(source) and source[i] !=target[j]:
                i+=1
                
            elif i==len(source) and rounds == 0:
                i = 0
                count+=1
                rounds = 1
                
            elif i==len(source) and rounds >=1:
                return -1
            
           
        return count+1
                
        

##ss
import math
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        
        arr = sorted(arr)
        pos = []
        neg = []
                
        
        for x in range(len(arr)):
            if arr[x] < 0:
                neg.append(arr[x])
                
            else:
                pos = arr[x:]
                break
                
        neg = neg[::-1]
        negdict,negtotal = self.make_dict(neg)
        posdict,postotal = self.make_dict(pos)
        
        #print(pos,neg,self.pos_check(posdict,postotal))
        return self.pos_check(posdict,postotal) and self.neg_check(negdict,negtotal)
        
    def make_dict(self,arr):
        dicts = {}
        total = 0
        for x in range(len(arr)):
            if arr[x] in dicts:
                dicts[arr[x]]+=1
                
            else:
                dicts[arr[x]] = 1
                
                
                
        return dicts,total
        
        
    def pos_check(self,dicts,total):
       
        for x in dicts:
            
            #print("inside",x,dicts,2*x in dicts)
            if dicts[x]!=0:
                if x == 0 and dicts[x]%2!=0:
                    return False
                
                elif x==0 and dicts[x]%2==0:
                    dicts[0] = 0

                elif x!=0 and 2*x not in dicts:
                    return False

                elif x!=0 and 2*x in dicts and dicts[2*x] >= dicts[x]:
                    #print("hello")
                    dicts[2*x]-=dicts[x]
                    dicts[x] = 0
                    
                elif x!=0 and 2*x in dicts and dicts[2*x] < dicts[x]:
                    return False
                
        for x in dicts:
            if dicts[x]!=0:
                return False
                
  
        return True
    
    def neg_check(self,dicts,total):
        
        for x in dicts:
            
            if dicts[x]!=0:
                if 2*x not in dicts:
                    return False

                elif 2*x in dicts and dicts[x]<=dicts[2*x]:
                    dicts[2*x]-=dicts[x]
                    dicts[x] = 0
                    
                elif 2*x in dicts and dicts[x] > dicts[2*x]:
                    return False
                
        for x in dicts:
            if dicts[x]!=0:
                return False
                
                
  
        return True
        
            
        

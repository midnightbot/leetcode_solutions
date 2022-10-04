##ss
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        index = 0
        ans = []
        while index < len(s):
            print("inside",index)
            #print(ans)
            if s.count(s[index]) == 1:
                ans.append(index)
                index+=1
              
            elif s.count(s[index]) > 1:
                last = self.find_last_index(s,s[index])
                #print(last)
                
                temp = []
                temp.append(last)
                temp2 = []
                queue = []
                queue = [s[z] for z in range(index,last)]
                ok = 0
                while queue:

                    for z in range(len(queue)):
                        node = queue.pop(0)
                        indx = (self.find_last_index(s,node))
                        
                        if indx < last:
                            temp.append((self.find_last_index(s,node)))
                        else:
                            ok = max(ok,indx)
                            temp.append((self.find_last_index(s,node)))
                            for m in range(last, ok):
                                temp2.append(s[m])
                            last = max(last,ok)
           
                    #print(temp2) 
                    #last = ok
                    queue = temp2
                    temp2 = []
     
                #print(temp)
                #print(temp)
                split = max(temp)
                
                ans.append(split)
                index = split +1
                
        finals = []
        finals.append(ans[0]+1)
        for x in range(1,len(ans)):
            finals.append(ans[x]-ans[x-1])
            
        return finals
            
            
        
    def find_last_index(self,s,a):
        
        for x in range(len(s)-1,-1,-1):
            if s[x] == a:
                return x
        

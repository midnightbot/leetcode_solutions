##ss
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        if n == 1:
            return ["0","1","8"]
        single = [0,1,8]
        dub = [6,9]
        ans = set()
        temp = [0 for x in range(n)]
        self.makenum(0,n-1,single,dub,temp,ans)
        comp = list(ans)
        #print(comp)
        comp = sorted(comp,key = lambda x:x[0])
        #print(comp)
        for x in range(len(comp)):
            if comp[x][0]!="0":
                break
                
        comp = comp[x:len(comp)]
        #print(comp)
        final = []
        for x in range(len(comp)):
            tmps =""
            for y in range(len(comp[x])):
                tmps+=comp[x][y]
                
            final.append(tmps)
            
        return final
    def makenum(self,start,end,single,dub,strs,ans):
        
        
        if start > end:
            tempo = ""
            for z in range(len(strs)):
                tempo+=str(strs[z])
                
            ans.add(tuple((tempo)))
            
        elif end - start == 0:
            for x in range(len(single)):
                #new_s = strs+str(single[x])
                new_s = copy.copy(strs)
                new_s[start] = single[x]
                self.makenum(start+1,end,single,dub,new_s,ans)
                
        else:
            #print(start)
            new_s = copy.copy(strs)
            new_s[start] = 6
            new_s[end] = 9
            
            new_s2 = copy.copy(strs)
            new_s2[start] = 9
            new_s2[end] = 6
            
            self.makenum(start+1,end-1,single,dub,new_s,ans)
            self.makenum(start+1,end-1,single,dub,new_s2,ans)
            
            for z in range(len(single)):
                new_ss = copy.copy(strs)
                new_ss[start] = single[z]
                new_ss[end] = single[z]
                self.makenum(start+1,end-1,single,dub,new_ss,ans)
            
        
        
        

##ss
##same as 247. Strobogrammatic Number II (make all number of digits less than or eqal to len(high)
##then using linear search on ans to see how many numbers are in range low to high
##there is better solution, but done it using 247
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        
        n = len(high)
        
        single = [0,1,8]
        dub = [6,9]
        ans = set()
        
        for x in range(n,1,-1):
            #print("inside")
            temp = [0 for x in range(x)]
            self.makenum(0,x-1,single,dub,temp,ans)
        
        
        comp = list(ans)
        final = []
        for x in range(len(comp)):
            tmps =""
            if comp[x][0]!="0":
                for y in range(len(comp[x])):
                    tmps+=comp[x][y]

                final.append(int(tmps))
        
        final = sorted(final)
        final.insert(0,0)
        final.insert(1,1)
        final.insert(2,8)
        for x in range(len(final)):
            if final[x] >= int(low):
                break
                
        for y in range(len(final)-1,-1,-1):
            if final[y] <= int(high):
                break
                
        return y-x+1
        #print(final)
        
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
        

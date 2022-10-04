##ss
class Solution:
    def sortString(self, s: str) -> str:
        
        ans = ""
        
        s = sorted(s)
        compare = []
        curr = s[0]
        count = 1
        for x in range(1,len(s)):
            if s[x]!=curr:
                compare.append([count,curr])
                count = 1
                curr = s[x]
                
            else:
                count+=1
        compare.append([count,curr])       
        this = 0
        temp = ""
        ops = 1
        #print(compare)
        while ops!=0:
            temp = ""
            ops = 0
            #print(ans)
            if this%2==0:
                for x in range(len(compare)):
                    if compare[x][0] > 0:
                        #print(compare[x][0])
                        ops+=1
                        temp+=compare[x][1]
                        compare[x][0]-=1
                        
                ans+=temp
                
            else:
                for x in range(len(compare)-1,-1,-1):
                    if compare[x][0] > 0:
                        ops+=1
                        temp+=compare[x][1]
                        compare[x][0]-=1
                        
                ans+=temp
                
                
            this+=1
        return ans
                    
        

        
        

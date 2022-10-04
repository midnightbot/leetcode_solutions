##ss
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        
        ## perm[i] < perm[i+1] -> I
        ## perm[i] > perm[i+1] -> D
        
        ## count number of continuous d's and just reverse the array of the range
        ## "DDI"
        ## example - > [1,2,3,4]
        ## for x in range(len(s))
        ## x = 0 dcount=1 [1,2,3,4]
        ## x= 1 dcount = 2 [1,2,3,4]
        ##x=2 -> reverse ans[x-dcount:x+1] -> [3,2,1,4]
        top = 1
        stack = [1]
        
        ans = [x for x in range(1,len(s)+2)]
        dcount = 0
        
        for x in range(len(s)):
            if s[x] == 'D':
                dcount+=1
                
            else:
                temp = ans[x-dcount:x+1]
                temp = temp[::-1]
                c = 0
                #print(temp)
                #print(x)
                for z in range(x-dcount,x+1,+1):
                    ans[z] = temp[c]
                    c+=1
                    
                dcount = 0
                    
            #print(ans)
            
        temp = ans[x-dcount+1:]
        temp = temp[::-1]
        c = 0
        #print(temp,x,dcount)
        #print(x)
        for z in range(x-dcount+1,len(ans),+1):
            ans[z] = temp[c]
            c+=1

        dcount = 0
        return ans
                
            
            

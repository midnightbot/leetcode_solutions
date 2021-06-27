class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        ans = [0,0,0,0,0]
        
        for x in range(len(text)):
            if text[x]=='b':
                ans[0]+=1
                
            elif text[x]=='a':
                ans[1]+=1
                
            elif text[x]=='l':
                ans[2]+=1
                
            elif text[x]=='o':
                ans[3]+=1
                
            elif text[x]=='n':
                ans[4]+=1
                
                
        if ans[2]%2==0:
            ans[2] = ans[2]/2
            
        else:
            ans[2] = int((ans[2]-1)/2)
            
            
        if ans[3]%2==0:
            ans[3] = ans[3]/2
            
        else:
            ans[3] = int((ans[3]-1)/2)
            
            
        return int(min(ans))
        

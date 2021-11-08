class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        self.combinations(1,[],output,k,n)
        return output
        ##total combinations will be nCk
        
    
    def combinations(self,start, ans,output,k,n):
        
        if len(ans) == k:
            #print(output)
            output.append(ans[:])
            
        for x in range(start,n+1):
            ans.append(x)
            
            self.combinations(x+1,ans,output,k,n)
            
            ans.pop()
            
            
        #print(output)
            
        
        
        

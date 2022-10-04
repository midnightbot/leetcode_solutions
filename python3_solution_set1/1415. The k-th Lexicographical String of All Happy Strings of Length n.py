##ss
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        self.ans = []
        
        def make_string(indx,strs):
            
            if indx == n:
                self.ans.append(strs)
                
            else:
                for x in ["a","b",'c']:
                    if x!=strs[-1]:
                        make_string(indx+1,strs+x)
                        
        
        make_string(1,"a")
        make_string(1,"b")
        make_string(1,"c")
        
        self.ans = sorted(self.ans)
        
        if len(self.ans) < k:
            return ""
        else:
            return self.ans[k-1]
        #print(self.ans)
        

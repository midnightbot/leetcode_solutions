##ss
##simple recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.gens(n,n,ans,"")
        return ans
    ##left,right
    def gens(self,m,n,ans,strs):
        ##return all combinatiosn of brackets with val = n
        #print(m,n,strs)
        if m == 0 and n ==0:
            #print(strs)
            ans.append(strs)
            
        else:
            if len(strs) == 0:
                self.gens(m-1,n,ans,strs+"(")
                
            else:
                c1 = strs.count("(")
                c2 = strs.count(")")
                if m == 0:
                    self.gens(0,n-1,ans,strs+")")
                    
                elif c1 == c2 and m>=1:
                    self.gens(m-1,n,ans,strs+"(")
                    
                elif c1 > c2 and m>=1:
                    self.gens(m-1,n,ans,strs+"(")
                    self.gens(m,n-1,ans,strs+")")
                    
                elif c1 > c2 and m==0:
                    self.gens(m,n-1,ans,strs+")")
            
        
        
        

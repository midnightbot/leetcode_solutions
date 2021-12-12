##ss
##Simple Dynamic Programming Solution
## Do as directed
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        ##'a' -> 'e'
        ##'e' -> 'a' or 'i'
        ##'i' not 'i'
        ## 'o' -> 'i' or 'u'
        ## 'u' -> 'a'
        if n == 1:
            return 5
        ans = []
        memo = {}
        self.form_words(n-1,"a",ans,memo) ##starting char can either be a
        self.form_words(n-1,"e",ans,memo) ##starting char can either be e
        self.form_words(n-1,"i",ans,memo) ##starting char can either be i
        self.form_words(n-1,"o",ans,memo) ##starting char can either be o
        self.form_words(n-1,"u",ans,memo) ##starting char can either be u
        
        t1 = memo[("e",n-1)]+memo[("a",n-1)] + memo[("i",n-1)] + memo[("o",n-1)] + memo[("u",n-1)]
        #print(ans)
        ##ans contains all the combinations
        return t1%(pow(10,9)+7)
    #@lru_cache(None)
    def form_words(self,n,strs,ans,memo):
        
        if n == 0: ##if no more space to add other character, that means 1 string is generated
            ans.append(strs)
            return 1
            
        elif (strs[len(strs)-1],n) in memo: ## if we have already computed this subproblem return directly
            return memo[(strs[len(strs)-1],n)]
        
        else:
            if strs[len(strs)-1] == "a": ##'a' -> 'e'
                temp = self.form_words(n-1,strs+"e",ans,memo)
                memo[("a",n)] = temp
                return memo[("a",n)]
                
            elif strs[len(strs)-1] == 'e': ##'e' -> 'a' or 'i'
                t1 = self.form_words(n-1,strs+"a",ans,memo)
                t2 = self.form_words(n-1,strs+"i",ans,memo)
                #memo[("a",n-1)] = t1
                memo[("e",n)] = t1 + t2
                return memo[("e",n)]
                
            elif strs[len(strs)-1] == 'i':  ##'i' not 'i'
                t1 = self.form_words(n-1,strs+"a",ans,memo)
                t2  = self.form_words(n-1,strs+"e",ans,memo)
                t3 = self.form_words(n-1,strs+"o",ans,memo)
                t4 = self.form_words(n-1,strs+"u",ans,memo)
                memo[("i",n)] = t1+t2+t3+t4
                return memo[("i",n)]
                
            elif strs[len(strs)-1] == 'o': ## 'o' -> 'i' or 'u'
                t1 = self.form_words(n-1,strs+"i",ans,memo)
                t2  = self.form_words(n-1,strs+"u",ans,memo)
                memo[("o",n)] = t1+t2
                return  memo[("o",n)]
                     
            else:## 'u' -> 'a'
                t1 = self.form_words(n-1,strs+"a",ans,memo)
                memo[("u",n)] = t1
                return memo[("u",n)]
                
                
        

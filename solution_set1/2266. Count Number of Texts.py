class Solution:
    def countTexts(self, pk: str) -> int:
        
        mods = 10 ** 9 + 7
        
        @lru_cache(None)
        def ways(indx):
            #print(indx)
            if indx == 0:
                return 1
            
            else:
                ans = ways(indx-1)
                #print(indx,"las")
                if indx-2>=0 and pk[indx-1] == pk[indx-2]:
                    ans+=ways(indx-2)
                    ans%=mods
                    
                if indx-3>=0 and pk[indx-1] == pk[indx-2] == pk[indx-3]:
                    ans+=ways(indx-3)
                    ans%=mods
                    
                if indx-4>=0 and pk[indx-1] in ["7","9"]:
                    if pk[indx-1] == pk[indx-2] == pk[indx-3] == pk[indx-4]:
                        ans+=ways(indx-4)
                        ans%=mods
                        
                return ans%mods
            
            
        return ways(len(pk))%mods
                    
                
        

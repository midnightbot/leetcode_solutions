class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        n = len(arr)
        
        @cache
        def find_ans(curr, indx):
            c=set(curr)
            
            if indx == n:
                return len(curr)
            
            else:
                ans = 0
                
                ans = max(ans, find_ans(curr,indx+1))
                wrd = arr[indx]
                done = False
                if len(set(wrd)) == len(wrd):
                
                    for it in wrd:
                        if it not in c:
                            continue
                        else:
                            done = True
                            break

                    if done == False:
                        ans = max(ans,find_ans(curr+wrd, indx+1))
                return ans
                    
        return find_ans("",0)
                        
        

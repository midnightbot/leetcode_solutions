##ss
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        final_ans = [float('inf')]
        
        
        def find_ans(indx, ans):
            if indx == len(cookies):
                final_ans[0] = min(final_ans[0], max(ans))
                
            if final_ans[0] <= max(ans): ## prune unnecessary branches
                return 
            else:
                for x in range(k):
                    ans[x]+= cookies[indx]
                    find_ans(indx+1, ans )
                    ans[x]-= cookies[indx]
                    
        find_ans(0, [0 for x in range(k)])
        return final_ans[0]
        

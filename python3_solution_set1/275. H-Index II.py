##ss
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        ## 'h' papers have more than 'h' citations
        ## rest 'n-h' paper have less than 'h' citations
        
        
        l = 0
        r = max(citations)
        
        def check(h):
            for x in range(len(citations)):
                if citations[x] >=h:
                    return len(citations) - x
                
            return 0
        
        ans  = []
        
        while l <= r:
            mid = (l+r) // 2
            
            if check(mid) >= mid:
                ans.append(mid)
                l = mid + 1
                
            else:
                r = mid - 1
           
        
        return max(ans) if len(ans)!=0 else 0
            

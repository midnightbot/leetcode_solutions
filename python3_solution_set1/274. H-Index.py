##ss
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ## 'h' papers have more than 'h' citations
        ## rest 'n-h' paper have less than 'h' citations
        
        
        l = 0
        r = max(citations)
        citations = sorted(citations)
        def check(h):
            for x in range(len(citations)):
                if citations[x] >=h:
                    return len(citations) - x
                
            return 0
        
        ans  = []
        #print(check(2))
        while l <= r:
            mid = (l+r) // 2
            #print(l,r,mid,check(mid))
            if check(mid) >= mid:
                ans.append(mid)
                l = mid + 1
                
            else:
                r = mid - 1
           
        #print(ans)
        return max(ans) if len(ans)!=0 else 0
        

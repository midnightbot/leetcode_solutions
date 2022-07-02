class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        
        hc = sorted(hc)
        vc = sorted(vc)
        
        hc.insert(0,0)
        vc.insert(0,0)
        hc.append(h)
        vc.append(w)
        temp1 = [hc[x+1]-hc[x] for x in range(len(hc)-1)]
        temp2 = [vc[x+1]-vc[x] for x in range(len(vc)-1)]
        
        return (max(temp1) * max(temp2)) % (10**9+7)
        
        

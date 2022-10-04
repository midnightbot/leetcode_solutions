##ss
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        ans = []
        ainit = sum(aliceSizes)
        binit = sum(bobSizes)
        
        adict = {}
        bdict = {}
        
        for x in range(len(aliceSizes)):
            if aliceSizes[x] in adict:
                adict[aliceSizes[x]].append(x)
                
            else:
                adict[aliceSizes[x]] = [x]
                
        for x in range(len(bobSizes)):
            if bobSizes[x] in bdict:
                bdict[bobSizes[x]].append(x)
                
            else:
                bdict[bobSizes[x]] = [x]
                
        #print(adict,bdict)
        
        total = ainit + binit
        
        afterswap = total // 2
        
        #print(afterswap)
        achange = afterswap - ainit
        
        for x in adict:
            if x + achange in bdict:
                return [x,x+achange]
        
        

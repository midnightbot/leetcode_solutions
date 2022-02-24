##ss
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        #print(pairs)
        ##follow example  [1,2] [3,4]
        ##simple dp
        pairs = sorted(pairs, key = lambda x:x[1])
        print(pairs)
        
        ans = 0
        compat = [1 for x in range(len(pairs))]
        
        for x in range(len(pairs)-2,-1,-1):
            
            for y in range(x,len(pairs)):
                if pairs[y][0] > pairs[x][1]:
                    compat[x] += compat[y]
                    break
                    
        return max(compat)
            
        
        
        
        
        

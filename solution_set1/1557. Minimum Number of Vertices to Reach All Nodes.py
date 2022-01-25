##ss
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        ##ans = nodes with 0 inedge
        
        incom = set()
        #all_list = 
        total = set([x for x in range(n)])
        for x in range(len(edges)):
            incom.add(edges[x][1])
            
            
        #print(incom)
        ans = total.difference(incom)
        return ans

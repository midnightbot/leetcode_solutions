##ss
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        ##similar to finding lowest common ancestor Q236
        ##only problem is this will be n-ary tree rather than binary tree
        ##so we can store parent of each node, it will be a kind of linked list
        ##store region1 to head in visited
        ##now keep going up region2 as soon as we something in visited, return it
        parent = {}
        
        for x in range(len(regions)):
            for y in range(1,len(regions[x])):
                parent[regions[x][y]] = regions[x][0]
                
        visited = set()
        req = region1
        
        while req in parent:
            visited.add(req)
            req = parent[req]
            
        req = region2
        
        while req in parent:
            if req in visited:
                return req
            req = parent[req]
        
        return req

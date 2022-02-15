class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        
        maps = {}
        
        for x in range(len(features)):
            maps[features[x]] = 0
            
        set1 = set(features)
        for x in range(len(responses)):
            #print(set(responses[x]))
            ans = set1.intersection(set(responses[x].split(" ")))
            for z in ans:
                maps[z]+=1
                
        maps = sorted(maps.items(), reverse= True, key = lambda x:x[1])
        maps = [maps[x][0] for x in range(len(maps))]
        
        return maps
        

##ss
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        dicts = {}
        ##company name: set(person indexs)
        
        ans = set()
        for x in range(len(favoriteCompanies)):
            for y in range(len(favoriteCompanies[x])):
                
                if favoriteCompanies[x][y] not in dicts:
                    dicts[favoriteCompanies[x][y]] = {x}    
                else:
                    dicts[favoriteCompanies[x][y]].add(x)
        #print(dicts)            
        for x in range(len(favoriteCompanies)):
            temp = dicts[favoriteCompanies[x][0]]
            for y in range(1,len(favoriteCompanies[x])):
                temp = temp.intersection(dicts[favoriteCompanies[x][y]])
            #print(temp)
            if len(temp) == 1:
                ans.add(x)
                    
            #print(ans)       
        return sorted(list(ans))
    

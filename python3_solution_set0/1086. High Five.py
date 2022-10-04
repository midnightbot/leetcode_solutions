##ss
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        
        items = sorted(items, key = lambda x:(x[0],-x[1]))
        
        dicts = {}
        
        for x in range(len(items)):
            if items[x][0] not in dicts.keys():
                dicts[items[x][0]] = [items[x][1]]
                
            elif items[x][0] in dicts.keys() and len(dicts[items[x][0]]) < 5:
                dicts[items[x][0]].append(items[x][1])
                
        ans = []
        
        for x in dicts.keys():
            ans.append([x,sum(dicts[x])//5])
            
        return ans
        

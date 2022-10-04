##ss
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        total_items = set()
        total_tables = set()
        for x in range(len(orders)):
            total_items.add(orders[x][2])
            total_tables.add(int(orders[x][1]))
            
        #print(total_items)
        #print(total_tables)
        total_tables = list(total_tables)
        #print(total_tables)
        total_tables = sorted(total_tables)
        #print(total_tables)
        
        total_items = list(total_items)
        total_items = sorted(total_items)
        
        total_items.insert(0,"Table")
        #print(total_items)
        
        fmap = {}
        tmap = {}
        ans = []
        for x in range(len(total_tables)):
            ans.append([0 for x in range(len(total_items))])
            ans[x][0] = total_tables[x]
        #print(ans)
        for x in range(len(total_tables)):
            tmap[total_tables[x]] = x
            
        for x in range(len(total_items)):
            fmap[total_items[x]] = x
            
        for x in range(len(orders)):
            ans[tmap[int(orders[x][1])]][fmap[orders[x][2]]]+=1
            
        ans.insert(0,total_items)
        for x in range(1,len(ans)):
            for y in range(len(ans[0])):
                ans[x][y] = str(ans[x][y])
                
        return ans

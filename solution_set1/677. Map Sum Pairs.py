##ss
class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
        
class MapSum:

    def __init__(self):
        self.root = Node()
        self.dicts = {}
        

    def insert(self, key: str, val: int) -> None:
        if key in self.dicts:
            self.dicts[key] = val
        else:
            self.dicts[key] = val
            
            ptr = self.root
            for y in key:
                if y not in ptr.children:
                    ptr.children[y] = Node()
                    
                ptr = ptr.children[y]
                
            ptr.isend = True
        
        

    def sum(self, prefix: str) -> int:
        ptr = self.root
        
        ans = 0
        tot = []
        for x in prefix:
            if x in ptr.children:
                ptr = ptr.children[x]
            else:
                return 0
            
        if ptr.isend == True:
            tot.append(prefix)
        queue = [(ptr,prefix)]
        while queue:
            #print(queue)
            for x in range(len(queue)):
                wrd = queue.pop(0)
                #if y in wrd[0].children:
                for y in wrd[0].children:
                    newp = copy.copy(wrd[0])
                    newp = newp.children[y]
                    if newp.isend == True:
                        tot.append(wrd[1]+y)

                    queue.append((newp,wrd[1]+y))
        
        for x in range(len(tot)):
            ans+=self.dicts[tot[x]]
            
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

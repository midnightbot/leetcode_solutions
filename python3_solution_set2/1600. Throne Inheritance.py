class ThroneInheritance:
    ## simple dfs question
    def do_dfs(self,visited, curr):
        if curr not in visited:
            if curr not in self.dead:
                self.order.append(curr)
            visited.add(curr)
            if curr in self.g:
                for chlds in self.g[curr]:
                    self.do_dfs(visited, chlds)

    def __init__(self, kingName: str):
        self.g = {}
        self.dead = set()
        self.g[kingName] = []
        self.king = kingName
        self.total = 0
        self.order = []
        ## key: kingname, value:[children]
        

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.g:
            self.g[parentName].append(childName)
        else:
            self.g[parentName] = [childName]
        self.total+=1

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.order = []
        self.do_dfs(set(), self.king)
        return self.order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

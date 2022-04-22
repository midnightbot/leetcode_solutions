##ss
class Node:
    def __init__(self,val=-1):
        self.children = {}
        self.isend = [False,val]
        
class FileSystem:

    def __init__(self):
        self.files = Node()
        

    def createPath(self, path: str, value: int) -> bool:
        comp = path[1:].split("/")
        ptr = self.files
        
        for indx,folder in enumerate(comp):
            if indx == len(comp) - 1:
                if folder in ptr.children:
                    return False
                else:
                    ptr.children[folder] = Node(value)
                    
                    return True
                
            
            
            if folder not in ptr.children:
                return False
                
            ptr = ptr.children[folder]
                
                
        

    def get(self, path: str) -> int:
        comp = path[1:].split("/")
        ptr = self.files
        for x in comp:
            if x not in ptr.children:
                return -1
            
            ptr = ptr.children[x]
            
        return ptr.isend[1]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

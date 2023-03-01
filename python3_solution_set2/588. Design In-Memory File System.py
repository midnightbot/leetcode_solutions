## simple trie question

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.content = False

class FileSystem:

    def __init__(self):
        self.root = Node()

    ## searching in trie
    def ls(self, path: str) -> List[str]:
        ptr = self.root
        cmp = path.split("/")
        cmp = cmp[1:]
        
        if cmp[0] in ptr.children:
            for x in cmp:
                ptr = ptr.children[x]

        if list(ptr.children.keys()) == []:
            if ptr.content!=False:
                return [cmp[-1]]
            else:
                return []
        else:
            return sorted(ptr.children)

    ## adding node in trie
    def mkdir(self, path: str) -> None:
        ptr = self.root
        wrds = path.split("/")
        wrds = wrds[1:]
        for x in wrds:
            if x not in ptr.children:
                ptr.children[x] = Node()

            ptr = ptr.children[x]
        ptr.content = False
        
    ## adding node and content to trie
    def addContentToFile(self, filePath: str, content: str) -> None:
        ptr = self.root
        wrds = filePath.split("/")
        wrds = wrds[1:]
        for x in wrds:
            if x not in ptr.children:
                ptr.children[x] = Node()

            ptr = ptr.children[x]
        #print(ptr.content)
        if ptr.content!=False:
            ptr.content+=content
        else:
            ptr.content = content

    ## reading a node value in trie
    def readContentFromFile(self, filePath: str) -> str:
        ptr = self.root
        wrds = filePath.split("/")
        wrds = wrds[1:]
        for x in wrds:
            if x not in ptr.children:
                ptr.children[x] = Node()

            ptr = ptr.children[x]
        return ptr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

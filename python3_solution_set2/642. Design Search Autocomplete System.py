class Node:
    def __init__(self):
        self.children = {}  ## maintain all its children
        self.count = 0 ## maintain frequency

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.query = ''
        for indx,s in enumerate(sentences):
            wrds = s
            ptr = self.root
            for x in wrds:
                if x not in ptr.children:
                    ptr.children[x] = Node()
                ptr = ptr.children[x]
            ptr.count = times[indx]

    ## insert the typed sentence in the system and increase its count by 1
    def insert_in_system(self, s):
        wrds = s
        ptr = self.root
        for x in wrds:
            if x not in ptr.children:
                ptr.children[x] = Node()
            ptr = ptr.children[x]
        ptr.count+=1

    def input(self, c: str) -> List[str]:

        if c == '#': ## sentence is complete, add it to trie
            self.insert_in_system(self.query)
            self.query = ''
            return []

        ## match the input query with prefix of stored queries till now
        ptr = self.root
        self.query+=c
        wrds = self.query
        for x in wrds:
            if x not in ptr.children:
                return []
            ptr = ptr.children[x]

        ## from this point explore all sentences
        ans = []
        q = [(ptr,self.query)]
        while q:
            root, cur_wrd = q.pop()
            if root.count!=0:
                ans.append([cur_wrd, root.count])

            for it in root.children:
                q.append([root.children[it], cur_wrd +it])
                
        ans = sorted(ans, key = lambda x:(-x[1],x[0]))
        ans = [x[0] for x in ans]
        return ans[:min(len(ans),3)]

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

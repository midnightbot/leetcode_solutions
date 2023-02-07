class Node:
    def __init__(self):
        self.children = {}
        self.isend = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ## simple trie quesion
        self.root = Node()

        def insert(word: str) -> None:
            ptr = self.root

            for x in word:
                if x not in ptr.children:
                    ptr.children[x] = Node()

                ptr = ptr.children[x]
            ptr.isend = True

        
        for it in folder:
            temp = it.split("/")
            temp = temp[1:]
            #temp = "".join(temp)
            insert(temp)

        #print(self.root.children['a'].isend)
        self.ans = []
        def find_ans(root, curr):

            if root.isend:
                self.ans.append(curr)

            else:
                for c in root.children:
                    find_ans(root.children[c], curr+"/"+c)

        find_ans(self.root, "")
        #print(self.ans)
        return self.ans

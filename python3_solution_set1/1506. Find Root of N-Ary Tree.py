##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        indegree = {}
        #ret_indx = 0
        for x in range(len(tree)):
            if tree[x].val not in indegree:
                indegree[tree[x].val] = [0,x]
                ret_indx = x
            for y in tree[x].children:
                if y.val in indegree:
                    indegree[y.val] = [2]
                    
                else:
                    indegree[y.val] = [1]
                    
        for x in indegree:
            if len(indegree[x]) == 2:
                return tree[indegree[x][1]]
        #return tree[ret_indx]
        

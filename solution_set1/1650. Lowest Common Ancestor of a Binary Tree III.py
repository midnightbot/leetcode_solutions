##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
##Space Complexity : O(1)
## Time Complexity : O(n)
##where n is number of nodes in tree
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        ##keep on going up until a common parent if found
        ##find len of p to root
        ##find len of q to root
        ##diff = abs(p-q)
        ##if len(p) > len(q) go up diff units on p,similarly on q
        ##now from here keep going forward one one step and see if parent is common
        node1 = copy.copy(p)
        node2 = copy.copy(q)
        size1 = 0
        size2 = 0
        while p!=None:
            size1+=1
            p = p.parent
            
        while q!=None:
            size2+=1
            q = q.parent
            
        if size1 == size2:
            return self.findcommon(node1,node2)
                
                
        elif size1 > size2:
            diff = size1 - size2
            for x in range(diff):
                node1 = node1.parent
                
            return self.findcommon(node1,node2)
        
        else:
            diff = size2 - size1
            for x in range(diff):
                node2 = node2.parent
                
            return self.findcommon(node1,node2)

    def findcommon(self,node1,node2):##node1 and node2 are at same dist from root
        
        while node1!=None:

            if node1.val == node2.val:
                return node1
                
            node1 = node1.parent
            node2 = node2.parent
        

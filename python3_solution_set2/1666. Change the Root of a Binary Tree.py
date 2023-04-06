"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':

        ## if curr.left then curr.right = curr.left
        ## curr.left = curr.parent
        ## curr.left.parent = curr
        ## curr.right.parent = curr

        def find_ans(curr, last):
            p = curr.parent
            curr.parent = last

            if curr.left == last:
                curr.left = None
            if curr.right == last:
                curr.right = None

            if curr == root:
                return curr

            if curr.left:
                curr.right = curr.left
            curr.left = find_ans(p, curr)
            return curr

        return find_ans(leaf, None)



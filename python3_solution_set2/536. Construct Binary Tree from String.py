# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        def make_tree(s):
            if s == '': ## base case
                return None

            this_node = ''
            last_ind = -1
            for x in range(len(s)):
                if s[x]!='(':
                    this_node+=s[x]
                else:
                    #last_indx = x
                    break

            temp = s[x:]
            childs = []
            balance = 0
            for x in range(len(temp)):
                if temp[x] == '(':
                    balance+=1
                if temp[x] == ')':
                    balance-=1

                if balance == 0:
                    childs.append(temp[0:x+1])
                    childs.append(temp[x+1:])
                    break

            childs = [x[1:-1] for x in childs]
            new_node = TreeNode()
            new_node.val = int(this_node)
            if len(childs) == 2:
                new_node.left = make_tree(childs[0])
                new_node.right = make_tree(childs[1])

            if len(childs) == 1:
                new_node.left = make_tree(childs[0])

            return new_node
            #return TreeNode()

        return make_tree(s)

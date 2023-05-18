# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """

        def find_ans(root):
            if root.left is None and root.right is None:
                return root.val

            else:
                ans = ''
                if root.left:
                    ans+= find_ans(root.left)

                if root.right:
                    ans+=find_ans(root.right)

                return ans
        
        strs = find_ans(root)
        return strs[k-1]

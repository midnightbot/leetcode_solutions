# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        ## simple question
        ## maintain an iterator for voyage array
        ## do dfs
        ## where node.right.val matcher the current voyage[i] there is a flip

        indx = 0

        q = [root]
        ans = []
        while q:
            top = q.pop()
            if top is None:
                continue

            if top and top.val!=voyage[indx]:
                return [-1]

            indx+=1
            if top.right and top.right.val == voyage[indx]:
                q.append(top.left)
                q.append(top.right)
                if top.left:
                    ans.append(top.val)

            else:
                q.append(top.right)
                q.append(top.left)

            

        return ans
        

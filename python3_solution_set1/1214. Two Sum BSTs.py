##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        

        def make_set(root):

            ans = set()
            q = [root]
            while q:
                for x in range(len(q)):
                    node = q.pop(0)
                    ans.add(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            return ans
                
            
        
        temp1 = make_set(root1)
        temp2 = make_set(root2)
        
        temp1 = list(temp1)
        
        for x in range(len(temp1)):
            if target - temp1[x] in temp2:
                return True
            
        return False
        

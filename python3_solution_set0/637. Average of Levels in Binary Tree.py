##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        queue = [root]
        
        while queue:
            sums = 0
            temp = []
            for x in range(len(queue)):
                sums+=queue[x].val
            ans.append(sums/len(queue))
            for x in range(len(queue)):
                node = queue.pop()
                if node.left!=None:
                    temp.append(node.left)
                if node.right!=None:
                    temp.append(node.right)
                    
                    
            queue = temp
            temp = []
        return ans

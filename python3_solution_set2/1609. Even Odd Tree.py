# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        ## bfs and evaluate
        q = [root]
        lvlnum = 0
        prevseen = 0
        while q:
            newq = []
            if lvlnum%2==0:
                prevseen = -float('inf')
            else:
                prevseen = float('inf')

            for x in q:
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)

                if lvlnum%2==0:
                    if prevseen < x.val and x.val%2!=0:
                        prevseen = x.val
                        continue
                    else:
                        return False
                else:
                    if prevseen > x.val and x.val%2==0:
                        prevseen = x.val
                        continue
                    else:
                        return False
            lvlnum+=1
            q = newq
        return True 

                

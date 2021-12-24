##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root == None:
            return []
        ans = []
        globalans = []
        self.expands(root,[],targetSum,globalans)
        return globalans
        
    def expands(self,root,ans,targetSum,globalans):
        
        #print(ans)
        #ans = []
       
        if root.left == None and root.right == None:
            ans.append(root.val)
            if sum(ans) == targetSum:
                #print(ans)
                globalans.append(ans)
            ans = []

        if root.left!=None:
            temp = copy.copy(ans)
            temp.append(root.val)
            self.expands(root.left,temp,targetSum,globalans)
            
            


        if root.right!=None:
            temp = copy.copy(ans)
            temp.append(root.val)
            self.expands(root.right,temp,targetSum,globalans)
            
        

##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = [root]
        
        ans = 0
        
        while q:
            ##filter q here
            ##width is only calculated from 1st not null node of that level
            ##eg q = [null,null,1,null,2,3,4,null,null] - > [1,null,2,3,4]
            ##therefore remove nullnodes from left and right end
            
            for z in range(len(q)):
                if type(q[z]) == type(TreeNode()):
                    break
                    
            q = q[z:]
            
            for z in range(len(q)-1,-1,-1):
                if type(q[z]) == type(TreeNode()):
                    break
            q = q[:z+1]
            
            if len(q) == 1 and type(q[0])!=type(TreeNode()):
                q = []
            thisans = 0
            for x in range(len(q)):
                node = q.pop(0)
                
                if type(node) == type(TreeNode()):
                    q.append(node.left)
                    q.append(node.right)
                    thisans+=1
                    
                elif type(node) == int:##integer represent number of null nodes
                    thisans+= node
                    if type(q[-1]) == int:##if previous appended nodes were also null, we can combine them together
                        q[-1]+= node * 2
                        
                    else:
                        q.append(node*2)
                        
                elif node is None:##if a node is null, it will produce +2 in lower level width
                    thisans+=1
                    q.append(2)
                    
            ans = max(ans,thisans)
                    
        return ans
        

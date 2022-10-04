##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        ##bfs rather than dfs
        
        ans = []
        temp_ans = []
        while root.val!=-101:
            #print(ans)
            queue = [root]
            #print(ans)
            temp_ans = []
            while queue:
                temp = []
                #print(queue)
                for x in range(len(queue)):
                    node = queue.pop(0)
                    
                    if node.val!=-101:
                        if node.left!=None and node.left.val!=-101:
                            temp.append(node.left)


                        if node.right!=None and node.right!=-101:
                            temp.append(node.right)

                        if (node.left==None and node.right==None) or ((node.left==None or node.left.val==-101) and (node.right==None or node.right.val==-101)):
                            temp_ans.append(node.val)
                            node.val = -101

                queue = temp
            ans.append(temp_ans)
        
        return ans
                    
                
        

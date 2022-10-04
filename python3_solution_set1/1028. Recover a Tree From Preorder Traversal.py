# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        ## preorder = root left right
        
        
        def make_tree(strs,level):
            
            if strs == "":
                return TreeNode(None)
            
            else:
                #print(strs,level)
                node = TreeNode()
                curr = 0 
                indxs = []
                
                for x in range(len(strs)):
                    if strs[x] == '-':
                        curr+=1
                        
                    else:
                        if curr == level + 1:
                            indxs.append(x)##
                        curr = 0
                        
                    
                #print(indxs,strs)
                if len(indxs) == 0:
                    #(strs,level,"child node")
                    node.val = int(strs)
                  
                    
                elif len(indxs) == 1:
                    node.val = int(strs[:indxs[0] - level-1])
                    node.left = make_tree(strs[indxs[0]:],level+1)
                  
                elif len(indxs) == 2:
                    #print(strs,indxs,strs[indxs[0]:indxs[1] - level-1],strs[indxs[1]:])
                    #print(strs[indxs[0]:indxs[1] - level-1],"left child")
                    #print(strs[indxs[1]:],"right child")
                    #print(make_tree(strs[indxs[1]:],level+1),"rightchildans")
                    #print("----")
                    node.val = int(strs[:indxs[0]-level-1])
                    node.left = make_tree(strs[indxs[0]:indxs[1] - level-1],level+1)
                    node.right = make_tree(strs[indxs[1]:],level+1)
                    
                #print(node)
                #print("--")
                return node
                #nodeval = int(s[:])
                
                    
            
            
        return make_tree(traversal,0)
            
        

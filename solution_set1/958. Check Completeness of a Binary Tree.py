##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        ##check for complete binary tree
        
        level = 0
        q = [root]
        sizes = []
        newq = []
        total = 0
        queue = [root]
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            total+=1
            
        #print(total)
        mains = []
        while q:
            sizes.append(len(q))
            #print(q,"start")
            newq = []
            for x in range(len(q)):
                node = q.pop(0)
                c = 0
                if node.left:
                    newq.append(node.left)
                    c+=1
                    
                if node.right:
                    newq.append(node.right)
                    c+=1
                    
                if level == total - 2:
                    if node.left:
                        mains.append(node.left.val)
                    else:
                        mains.append(None)
                    if node.right:
                        mains.append(node.right.val)
                    else:
                        mains.append(None)
                    
                
                
            q = newq
            
            level+=1
         
        #print(sizes)
        #print(mains)
        for x in range(len(sizes)-1):
            if sizes[x]!=pow(2,x):
                return False
           
        start = -1
        end  = -1
        for x in range(len(mains)):
            if mains[x] == None:
                start = x
                break
        for x in range(len(mains)-1,-1,-1):
            if mains[x]!=None:
                end = x
                break
        
        #print(start,end)
        return (start==-1) or (start > end)
                

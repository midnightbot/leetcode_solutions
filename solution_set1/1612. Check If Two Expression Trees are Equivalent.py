##ss
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        
        #t2 = [0 for x in range(26)]
        return self.compare(self.evalss(root1),self.evalss(root2))
        ##as it is addition we just need to check if variables are same
        
        
    def evalss(self,root):
        t1 = [0 for x in range(26)]
        q = [root]
        
        while q:
            node = q.pop(0)
            chrs = node.val
            
            if ord(chrs)>=97 and ord(chrs)<=122:
                t1[ord(chrs)-ord('a')]+=1
                
            if node.left:
                q.append(node.left)
                
                
            if node.right:
                q.append(node.right)
                
        return t1
        
    def compare(self,t1,t2):
        
        for x in range(26):
            if t1[x]!=t2[x]:
                return False
            
            
        return True

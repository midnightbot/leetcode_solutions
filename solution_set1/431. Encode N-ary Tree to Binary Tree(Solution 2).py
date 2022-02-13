##ss
##Using serialization and deserialization technique from 428. Serialize and Deserialize N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        
        if root is None:
            return None
        def make_ans(root):
            
            thisans = ""
            thisans+="("
            thisans+=str(root.val)
            if root.children:
                for z in root.children:
                    thisans+= make_ans(z)
                    
            thisans+=")"
            
            return thisans
        ans = make_ans(root)
        node = TreeNode([ans],None,None)
        return node
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        
        if data is None:
            return None
        
        data = data.val[0]
        #print(data)
        
        if data == "":
            return None
        def make_tree(data):
            data = data[1:len(data)-1]
            #print("hi")
            nodeval = ""
            x = 0
            #print(data,"last",len(data),x)
            while x < len(data) and ord(data[x])>=48 and ord(data[x])<=57:
                nodeval+=data[x]
                x+=1
                
            balance = 0
            prev = x
            childs = []
            ##wherever count('(') == count(')') it will be a child of current root
            for y in range(x,len(data)):
                
                if data[y] == "(":
                    balance+=1
                    
                elif data[y] == ")":
                    balance-=1
                
                if balance == 0:
                    childs.append(data[prev:y+1])
                    prev = y+1
                    
            newnode = Node(nodeval,[])
            if len(childs) > 0:
                for z in childs:
                    newnode.children.append(make_tree(z))
                    
            return newnode
        return make_tree(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

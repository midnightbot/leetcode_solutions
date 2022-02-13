##ss
##Attempt 1
##solution is correct if all node values are unique, but if nodes have duplicate values it will get stuck due to dictionary call in decode
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
        #print(type(root.children))
        if root is None:
            return root
        q = [[root,-1]]
        comp = []
        
        while q:
            node = q.pop(0)
            comp.append([node[0].val,node[1]])
            
            if node[0].children:
                for z in node[0].children:
                    q.append([z,node[0].val])
                    
        
        def make_tree(comp,pointer):
            
            if pointer < len(comp):
                newnode = TreeNode((comp[pointer][0],comp[pointer][1]),None,None)
                newnode.right = make_tree(comp,pointer+1)
                
                return newnode
          
        #print(comp)
        return make_tree(comp,0)
        ##tree only has right child,left child always pointed to null
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        #print(data)
        if data is None:
            return data
        arr = []
        q = [data]
        
        while q:
            node = q.pop(0)
            arr.append(node.val)
            
            if node.right:
                q.append(node.right)
                
        child = {}
        for x in range(len(arr)):
            if arr[x][1] not in child:
                child[arr[x][1]] = [arr[x][0]]
                
            else:
                child[arr[x][1]].append(arr[x][0])
        #q = [child[-1]]
        #print(child)
        def make_tree(root):
            #print(root)
            newnode = Node(root,[])
            if root in child:
                #print(child[root])
                for z in range(len(child[root])):
                    k = child[root].pop(0)
                    newnode.children.append(make_tree(k))
                    
                if root in child and len(child[root])==0:
                    child.pop(root)
            return newnode
        
        return make_tree(child[-1][0])
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

##Attempt2
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
        
        if not root:
            return None
        
        node = TreeNode(root.val,None,None)
        if len(root.children) > 0:
            chld = root.children[0]
            node.left = self.encode(chld)
            
        curr = node.left
        
        for x in range(1,len(root.children)):
            curr.right = self.encode(root.children[x])
            curr = curr.right
            
        return node
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        
        if not data:
            return None
        
        node = Node(data.val, [])
        curr = data.left
        
        while curr:
            node.children.append(self.decode(curr))
            curr = curr.right
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

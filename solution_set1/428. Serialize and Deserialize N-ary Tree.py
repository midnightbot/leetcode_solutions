##fully ss:)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ""
        def make_ans(root):
            
            thisans = ""
            thisans+="("
            thisans+=str(root.val)
            if root.children:
                for z in root.children:
                    thisans+= make_ans(z)
                    
            thisans+=")"
            #thisans+=','
            return thisans
        return make_ans(root)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        #print("original",data)
        #print(data)
        
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
# codec.deserialize(codec.serialize(root))

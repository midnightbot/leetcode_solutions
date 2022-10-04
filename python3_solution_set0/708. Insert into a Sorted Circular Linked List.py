"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        node = Node()
        node.val = insertVal
        if head == None:
            node.next = node
            return node
        
        temp = head
        while temp.next!=head:
            if temp.val <= insertVal and insertVal <= temp.next.val:
                break
                
            elif temp.val > temp.next.val:
                if temp.val >= insertVal and temp.next.val >= insertVal:
                    break
                    
                if temp.val <= insertVal and temp.next.val <= insertVal:
                    break
                    
            temp = temp.next
            
        node.next = temp.next
        temp.next = node
        return head
            

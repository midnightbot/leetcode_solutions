##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        
        mid = self.find_mid(head)
        
        node = TreeNode(mid.val)
        
        if head == mid:##if this is the single element in this left, just return it
            return node
        
        else:##else divide linked list in the middle to get left and right childs
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(mid.next)
            
            return node
        

    def find_mid(self,head): ##helps in finding the middle node of the linked list
        
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev:
            prev.next = None
            
            
        return slow
        
        
        
        
        

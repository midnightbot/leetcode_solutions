##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        carry = 0
        
        ##step 1: rev linked list
        root = None
        while head:
            nextnode = head.next
            head.next = root
            root = head
            head = nextnode
            
        #print(root)
        
        ##step2 : add one now to head
        oldroot = root
        init = root
        count  = 0 
        while root:
            if root.val!=9:
                break
                
            else:
                count+=1
                
            root = root.next
        prevs = root
        for x in range(count):
            oldroot.val = 0
            prevs = oldroot
            oldroot = oldroot.next
        
        if oldroot:
            oldroot.val+=1
        else:
            nexs = ListNode(1)
            prevs.next = nexs
        
        #print(init)
        ##step 3 reverse linked list again
        root = None
        while init:
            nextnode = init.next
            init.next = root
            root = init
            init = nextnode
            
        return root
        ##reverse init
        #print()
            
                

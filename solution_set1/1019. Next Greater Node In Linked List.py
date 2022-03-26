##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        comp = []
        stack = []
        while head:
            comp.append(head.val)
            head = head.next
            
        ans = [0 for x in range(len(comp))]
        #print(comp)
        stack.append(comp[-1])
        for x in range(len(comp)-2,-1,-1):
            for z in range(len(stack)-1,-1,-1):
                if stack[z] > comp[x]:
                    ans[x] = stack[z]
                    #stack.append(comp[x])
                    break
                    
                else:
                    stack.pop()
                    
            stack.append(comp[x])
            #print(stack)
        
        return ans

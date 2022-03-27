##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        nodes = []
        
        while head:
            nodes.append(head.val)
            head = head.next
            
        
        
        n = len(nodes)
        
        common = n // k
        left = n % k
        sizes = [common for x in range(k)]
        for x in range(left):
            sizes[x]+=1
            
        for x in range(1,len(sizes)):
            sizes[x] += sizes[x-1]             
        
        make = []
        start = 0
        for x in range(len(sizes)):
            make.append([start,sizes[x]])
            start = sizes[x]
            
        #print(make,sizes)
        def makelist(pos,arr):
            if len(arr) == 0:
                return None
            if pos == len(arr) - 1:
                return ListNode(arr[pos])
            
            else:
                newnode = ListNode(arr[pos])
                newnode.next = makelist(pos+1,arr)
                
                return newnode
            
        result = []
        
        for x in range(len(make)):
            result.append(makelist(0,nodes[make[x][0]:make[x][1]]))
            
        return result

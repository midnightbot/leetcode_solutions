# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        

        def convert(node):
            ans = {}
            while node:
                ans[node.power] = node.coefficient
                node = node.next
            return ans

        def combine(l1, l2):
            ans = {}

            for x in l1:
                if x in l2:
                    ans[x] = l1[x] + l2[x]
                else:
                    ans[x] = l1[x]

            for x in l2:
                if x not in l1:
                    ans[x] = l2[x]

            ans = [[x,ans[x]] for x in ans]
            ans = sorted(ans, key = lambda x:-x[0])
            result = []
            for x,y in ans:
                if y!=0:
                    result.append([x,y])

            return result
        temp1 = convert(poly1)
        temp2 = convert(poly2)
        anss = combine(temp1, temp2)
        n = len(anss)

        def make_list(i):
            if i == n:
                return None

            else:
                new_node = PolyNode()
                new_node.power = anss[i][0]
                new_node.coefficient = anss[i][1]
                new_node.next = make_list(i+1)
                return new_node

        return make_list(0)
        #print(anss)

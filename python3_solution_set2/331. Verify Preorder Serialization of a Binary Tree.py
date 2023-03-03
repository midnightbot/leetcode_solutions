class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        ## no three # can be together

        stack = []

        comp = preorder.split(',')

        for it in comp:
            stack.append(it)

            while len(stack)>2 and stack[-1] == stack[-2] == '#' and stack[-3]!='#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')

        return stack == ['#']
        

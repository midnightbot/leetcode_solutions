class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = '+'
        num = 0

        for i, c in enumerate(s+'+'):
            if c not in '+-*/() ':
                num = num * 10 + (ord(c) - ord('0'))

            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'

            elif c in "*-+/)":
                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)


                elif sign == '/':
                    stack.append(int(float(stack.pop() / num)))

                elif sign == '*':
                    stack.append(stack.pop() * num)

                if c == ')':
                    num = 0
                    item = stack.pop()
                    while item!='(':
                        num+=item
                        item = stack.pop()
                    sign = stack.pop()

                else:
                    num = 0
                    sign = c
        #print(stack)
        return int(sum(stack))

        

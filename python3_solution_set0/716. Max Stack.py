class MaxStack:
    
    stack = []
    
    def __init__(self):
        global stack 
        stack = []
        

    def push(self, x: int) -> None:
        stack.append(x)
        

    def pop(self) -> int:
        return stack.pop(len(stack)-1)
        

    def top(self) -> int:
        return stack[len(stack)-1]
        

    def peekMax(self) -> int:
        return max(stack)
        

    def popMax(self) -> int:
        temp = max(stack)
        for x in range(len(stack)-1,-1,-1):
            if stack[x] == temp:
                stack.pop(x)
                break
                
        return temp


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

import abc 
from abc import ABC, abstractmethod 


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        else:
            return self.left.evaluate() // self.right.evaluate()

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        curr = None
        stack = []
        for i in postfix:
            curr = TreeNode(i)
            if not i.isdigit():
                curr.right = stack.pop()
                curr.left = stack.pop()
            stack.append(curr)
        return curr
        

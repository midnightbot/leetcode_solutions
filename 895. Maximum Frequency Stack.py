class FreqStack:
    def __init__(self):
        self.fmap = Counter()
        self.stack = [0]

    def push(self, x: int) -> None:
        self.fmap[x] += 1
        freq = self.fmap[x]
        if (freq == len(self.stack)): self.stack.append([x])
        else: self.stack[freq].append(x)

    def pop(self) -> int:
        top = self.stack[-1]
        x = top.pop()
        if (not top): self.stack.pop()
        self.fmap[x] -= 1
        return x

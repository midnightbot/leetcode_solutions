class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.output = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.output.append(val)
        
        if len(self.output) < self.size:
            return sum(self.output)/len(self.output)
        else:
            return sum(self.output[-1*self.size:])/self.size

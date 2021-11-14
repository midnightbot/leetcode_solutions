class CombinationIterator:

    queue = []
    def __init__(self, characters: str, combinationLength: int):
        global queue
        queue = []
        self.generate(characters, 0, "",combinationLength,queue) ##generating all combinations
        #print(queue)

    def next(self) -> str:
        return queue.pop(0) ##returns the generated combination in order

    def hasNext(self) -> bool:
        return queue ## Tells if queue is empty or not
        
    def generate(self,characters,start,strs,combinationLength,queue):
        if combinationLength == 0:
            queue.append(strs)
            return
        
        for i in range(start,len(characters)):
            self.generate(characters,i+1,strs+str(characters[i]),combinationLength-1,queue)
        

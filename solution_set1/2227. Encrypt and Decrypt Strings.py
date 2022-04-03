##ss
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], d: List[str]):
        
        self.fmap = {x:[] for x in keys}
        self.rmap = {x:[] for x in values}
        
        for x in range(len(keys)):
            self.fmap[keys[x]].append(values[x])
            self.rmap[values[x]].append(keys[x])
            
        
        
        self.temp = Counter(self.encrypt(x) for x in d)
        

    def encrypt(self, word1: str) -> str:
        result = ""
        for x in word1:
            result+=self.fmap[x][0]
            
        return result
        

    def decrypt(self, word2: str) -> int:
        
        return self.temp[word2]
            
        
    
        
        
        
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

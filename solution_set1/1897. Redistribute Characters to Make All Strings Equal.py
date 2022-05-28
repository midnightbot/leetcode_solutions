class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        return sum([y%len(words)==0 for y in Counter("".join([x for x in words])).values()]) == len(Counter("".join([x for x in words])).keys())
        
        

##ss
class MagicDictionary:

    def __init__(self):
        
        self.maps = {chr(x+ord('a')):set() for x in range(26)}
        self.maps['.'] = set()
        self.words = set()
        self.fmaps = {}
    def buildDict(self, dictionary: List[str]) -> None:
        
        for x in range(len(dictionary)):
            self.words.add(dictionary[x])
            for y in range(len(dictionary[x])):
                news = dictionary[x][0:y] + '.' + dictionary[x][y+1:]
                self.maps[news[0]].add(news)
                if news in self.fmaps:
                    self.fmaps[news].add(dictionary[x])
                else:
                    self.fmaps[news] = {dictionary[x]}
        #print(self.maps)
        

    def search(self, searchWord: str) -> bool:
        
        for x in range(len(searchWord)):
            news = searchWord[0:x] + '.' + searchWord[x+1:]
            #print(news in self.maps[news[0]], news[0])
            if news in self.maps[news[0]] and (searchWord not in self.fmaps[news] or len(self.fmaps[news]) > 1):
                return True
            
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

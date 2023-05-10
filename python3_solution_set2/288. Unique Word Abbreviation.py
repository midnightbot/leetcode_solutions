class ValidWordAbbr:
    def find_abbr(self,strs):
        if len(strs) == 2:
            return strs
        else:
            return strs[0] + str(len(strs)-2) +strs[-1]

    def __init__(self, d: List[str]):
        self.maps = {}
        for it in d:
            abbr = self.find_abbr(it)
            if abbr in self.maps:
                self.maps[abbr].add(it)
            else:
                self.maps[abbr] = {it}
        
    def isUnique(self, word: str) -> bool:
        ## condition1
        abbr = self.find_abbr(word)
        if abbr not in self.maps:
            return True

        ## condition2
        if abbr in self.maps:
            return len(list(self.maps[abbr])) == 1 and list(self.maps[abbr])[0] == word

        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count =0
        if ruleKey =="type":
            anss =0
        elif ruleKey =="color":
            anss = 1
        else:
            anss =2
            
        for x in range(len(items)):
            if items[x][anss] == ruleValue:
                count+=1
        return count

##ss
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        dict1 = {}
        dict2 = {}
        
        temp1 = s1.split(" ")
        temp2 = s2.split(" ")
        
        for x in temp1:
            if x in dict1:
                dict1[x]+=1
                
            else:
                dict1[x] = 1
                
        for x in temp2:
            if x in dict2:
                dict2[x]+=1
                
            else:
                dict2[x] = 1
                
        ans = []
        
        for x in dict1:
            if dict1[x] == 1 and x not in dict2:
                ans.append(x)
                
        for x in dict2:
            if dict2[x] == 1 and x not in dict1:
                ans.append(x)
                
        return ans
        

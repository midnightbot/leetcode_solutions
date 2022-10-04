##ss
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        
        ##each number can only be used once
        ##atmost uselimit items of same labels
        
        ##size is numwanted
        
        dicts = {}
        
        for x in range(len(labels)): ##mapping values to their labels
            if labels[x] not in dicts.keys():
                dicts[labels[x]] = [values[x]]
                
            else:
                dicts[labels[x]].append(values[x])
                
        for x in dicts.keys(): ##sorting values of each of the labels
            dicts[x] = sorted(dicts[x],reverse = True)
            
        #print(dicts)
        
        ans = []
        
        tempo = []
        for x in dicts.keys():
            for y in range(min(useLimit,len(dicts[x]))):##there can only be useLimit number of lables of same category
                tempo.append(dicts[x][y])
                
        tempo = sorted(tempo,reverse = True)##we want subarray with maximum sum, hence sort in reversed order
        
        return sum(tempo[0:numWanted]) ## return sum of first numWanted numbers
        
        

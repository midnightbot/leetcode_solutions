##ss
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        dicts = {}
        
        for x in range(len(strings)):
            temp = ""
            if len(strings[x]) == 1:
                #temp.append(-55)
                temp+="-55"
            else:
                for y in range(1,len(strings[x])):
                    
                    #temp.append((ord(strings[x][y])-ord(strings[x][y-1]))%26)
                    temp+= str((ord(strings[x][y])-ord(strings[x][y-1]))%26) + str(",")
            
            if temp in dicts.keys():
                dicts[temp].append(strings[x])
                
            else:
                dicts[temp] = [strings[x]]
                
                
        print(dicts)
            #temp.append(strings[x])       
            #nums.append(temp)
        ans = []
        for x in dicts.keys():
            ans.append(dicts[x])
            
        return ans
        #print(nums)
        
        
                
        

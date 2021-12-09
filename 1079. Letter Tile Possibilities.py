from itertools import combinations
import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = {}
        self.combinations(tiles,0,ans,"")
        print(ans)
        anss = 0
        final = set()
        for x in ans.keys():
            permutations = set(itertools.permutations(x)) ##finding all possible permutations of each string
            #for z in range(len(permutation))
            final |= permutations
            
        return len(final)
        
        
        
    def combinations(self,tiles,counter,ans,strs): ##finding all possible strings that can be formed
        ##strings can only be formed in forward direction
        ##eg "AAB"  - > 'A', 'AA', 'AB', 'B', "AAB"  -. then we will find all possible combinations of these strins
        ##eg combinations of "AAB" -> "AAB", "ABA", "BAA",..
        #print(ans,strs,counter)
        if counter < len(tiles):
            strs+= tiles[counter]
            if strs not in ans.keys():
                ans[strs] = 1
                #ans |= set(tuple((strs,1)))
                
            counter+=1    
            self.combinations(tiles,counter,ans,strs)
            self.combinations(tiles,counter,ans,strs[0:len(strs)-1])
            
        else:
            return ans
        
        
        

##ss
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        el1 = tops[0]
        el2 = bottoms[0]
        
        ##case1 tops all equal = el1
        ##case2 tops all equal = el2
        ##case3 bottoms all equal = el1
        ##case4 bottoms all equal = el2
        return min(self.find_count(tops,bottoms,el1),self.find_count(tops,bottoms,el2),self.find_count(bottoms,tops,el1),self.find_count(bottoms,tops,el2)) if min(self.find_count(tops,bottoms,el1),self.find_count(tops,bottoms,el2),self.find_count(bottoms,tops,el1),self.find_count(bottoms,tops,el2))!=float('inf') else -1
        
    def find_count(self,arr1,arr2,elem):
        
        count = 0
        
        for x in range(len(arr1)):
            if arr1[x] == elem:
                continue
                
            elif arr2[x] == elem:
                count+=1
                
            else:
                return float('inf')
            
        return count

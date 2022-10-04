##ss
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight = sorted(weight)
        bag = 0
        app = 0
        #print(weight)
        for x in range(len(weight)):
            if bag + weight[x] <= 5000:
                app+=1
                bag+=weight[x]
                
            else:
                break
                
        return app
        

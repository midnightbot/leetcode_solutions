##ss
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        count = n
        i = 0
        while count!=0 and i <= len(flowerbed)-1:
            
            if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1 
                count-=1
                
            elif i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[0] = 1
                count-=1
            elif flowerbed[i] == 0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                flowerbed[i] = 1
                count-=1
                
            i+=1
        
        if count == 0:
            return True
        
        else:
            return False

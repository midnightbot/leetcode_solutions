##ss
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        ans = keysPressed[0]
        anss = releaseTimes[0]
        
        for x in range(1,len(releaseTimes)):
            if releaseTimes[x] - releaseTimes[x-1] > anss:
                anss = releaseTimes[x] - releaseTimes[x-1]
                ans = keysPressed[x]
                
                
            elif releaseTimes[x] - releaseTimes[x-1] == anss and ord(keysPressed[x]) > ord(ans):
                ans = keysPressed[x]
                
        return ans
        

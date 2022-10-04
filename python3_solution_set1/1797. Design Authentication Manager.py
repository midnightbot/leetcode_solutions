##ss
class AuthenticationManager:

    def __init__(self, t: int):
        self.maxs = t
        self.maps = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.maps[tokenId] = currentTime + self.maxs
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if tokenId in self.maps and self.maps[tokenId] > currentTime:
            self.maps[tokenId] = currentTime + self.maxs
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for x in self.maps:
            if self.maps[x] > currentTime:
                c+=1
                
        return c
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

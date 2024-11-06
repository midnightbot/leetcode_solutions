class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        return ((ord(c1[0])-ord('a') + int(c1[1]))%2==0 and (ord(c2[0])-ord('a') + int(c2[1]))%2==0) or ((ord(c1[0])-ord('a') + int(c1[1]))%2!=0 and (ord(c2[0])-ord('a') + int(c2[1]))%2!=0)
        

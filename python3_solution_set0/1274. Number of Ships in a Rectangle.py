##ss
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        ans = []
        self.seeships(sea,topRight,bottomLeft,ans)
        
        return len(ans)
        
    def seeships(self,sea,tr,bl,ans):
        #print(tr.x,tr.y,bl.x,bl.y)
        if ((bl.x < tr.x and bl.y < tr.y)or (bl.x <= tr.x and bl.y < tr.y) or (bl.x < tr.x and bl.y <= tr.y) ) and sea.hasShips(tr,bl) == True:
            tx = tr.x
            ty = tr.y
            bx = bl.x
            by = bl.y
            midsx = (tx+bx)//2
            midsy = (ty+by)//2
            
            self.seeships(sea,Point(midsx,midsy),bl,ans)
            self.seeships(sea,Point(tx,midsy),Point(midsx+1,by),ans)
            self.seeships(sea,Point(midsx,ty),Point(bx,midsy+1),ans)
            self.seeships(sea,tr,Point(midsx+1,midsy+1),ans)
        
        elif tr.x == bl.x and tr.y == bl.y and sea.hasShips(tr,bl) == True:
            #print(tr.x,tr.y)
            ans.append(1)
        

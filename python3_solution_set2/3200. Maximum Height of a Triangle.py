class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans = 0

        row = 1
        possible = True
        rr = red
        bb = blue
        while possible:
            if red >= row:
                red-=row
                row+=1
                if blue >= row:
                    blue-=row
                    row+=1
                else:
                    possible = False

            else:
                possible = False
        ans = max(ans, row)
        row = 1
        possible = True
        while possible:
            if bb >= row:
                bb-=row
                row+=1
                if rr >= row:
                    rr-=row
                    row+=1
                else:
                    possible = False

            else:
                possible = False  

        ans = max(ans, row)    
        return ans-1
        

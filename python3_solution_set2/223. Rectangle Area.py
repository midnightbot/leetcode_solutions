class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def find_area(a,b,c,d):
            return abs(c-a) * abs(d-b)

        
        xdict = []
        ydict = []
        xoverlap = 0
        xdict.append([ax1,1])
        xdict.append([ax2,-1])
        xdict.append([bx1,1])
        xdict.append([bx2,-1])

        arr1 = [[x[0],x[1]] for x in xdict]
        arr1 = sorted(arr1, key = lambda x:x[0])

        if arr1[0][1] == arr1[1][1] == 1:
            xoverlap = abs(arr1[1][0] - arr1[2][0])

        yoverlap = 0
        ydict.append([ay1,1])
        ydict.append([ay2,-1])
        ydict.append([by1,1])
        ydict.append([by2,-1])

        arr1 = [[x[0],x[1]] for x in ydict]
        arr1 = sorted(arr1, key = lambda x:x[0])

        if arr1[0][1] == arr1[1][1] == 1:
            yoverlap = abs(arr1[1][0] - arr1[2][0])

        #print(arr1)
        return find_area(ax1,ay1,ax2,ay2) + find_area(bx1,by1,bx2,by2) - (xoverlap*yoverlap)

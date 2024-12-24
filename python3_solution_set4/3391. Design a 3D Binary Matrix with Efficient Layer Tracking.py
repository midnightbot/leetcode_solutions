class Matrix3D:

    def __init__(self, n: int):
        self.mat = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
        self.x_count = {x:0 for x in range(n)}
        
    
    def setCell(self, x: int, y: int, z: int) -> None:
        if self.mat[x][y][z]!=1:
            self.mat[x][y][z] = 1
            self.x_count[x]+=1
        

    def unsetCell(self, x: int, y: int, z: int) -> None:
        if self.mat[x][y][z]!=0:
            self.mat[x][y][z] = 0
            self.x_count[x]-=1
        

    def largestMatrix(self) -> int:
        # print(self.x_count)
        ans = 0
        maxs = 0
        for it in self.x_count:
            if self.x_count[it] >= maxs:
                maxs = self.x_count[it]
                ans = max(ans, it)
        return ans
        


# Your Matrix3D object will be instantiated and called as such:
# obj = Matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()

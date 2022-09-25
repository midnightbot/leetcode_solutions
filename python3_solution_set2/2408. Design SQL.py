class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        
        self.data = {x:{} for x in names}
        self.indx = {x:1 for x in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        self.data[name][self.indx[name]] = row
        self.indx[name]+=1
        
    def deleteRow(self, name: str, rowId: int) -> None:
        self.data[name].pop(rowId)
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.data[name][rowId][columnId-1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)

class LogSystem:

    def __init__(self):
        self.logs = []
        

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append([id, timestamp])
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        indx = {'Year': 5, 'Month': 8, 'Day': 11, 'Hour': 14, 'Minute': 17, 'Second': 20}
        i = indx[granularity]
        start = start[:i]
        end = end[:i]

        return sorted(list(set(sorted([id for id,timestamp in self.logs if start<=timestamp[:i]<=end]))))
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

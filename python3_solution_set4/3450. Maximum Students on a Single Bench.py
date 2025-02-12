class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        maps = {}

        for x,y in students:
            if y not in maps:
                maps[y] = set()

            maps[y].add(x)

        return max([len(maps[x]) for x in maps] + [0])

        

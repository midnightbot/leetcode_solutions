##ss
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        logs = sorted(logs,key=lambda x:x[0])
        print(logs)
        ans = [0 for x in range(k)]
        dicts = {}
        visited = []
        for x in range(len(logs)):
            if logs[x][0] not in visited:
                visited.append(logs[x][0])
                temp = set()
                for y in range(x,len(logs)):
                    if logs[y][0] > logs[x][0]:
                        break
                        
                    else:
                        temp.add(logs[y][1])
                        #temp2 = set(logs[y][1])
                        #temp.add(set(logs[y][1]))
                        
                dicts[logs[x][0]] = temp
        
        counts = [0 for x in range(k)]
        for x in dicts.keys():
            counts[len(dicts[x])-1]+=1
            
        return counts

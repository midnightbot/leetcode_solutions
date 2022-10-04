##ss
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        dicts = {}
        
        for x in range(len(queries)):
            t1 = 0
            t2 = 0
            if (queries[x][0],queries[x][1]) in dicts.keys():
                ans.append(dicts[(queries[x][0],queries[x][1])])
            else:
                for m in range(queries[x][0],-1,-1):
                    if colors[m] == queries[x][1]:
                        t1 = 1
                        break

                for n in range(queries[x][0],len(colors)):
                    if colors[n] == queries[x][1]:
                        t2 = 1
                        break

                if t1==0 and t2==0:
                    ans.append(-1)
                    dicts[(queries[x][0],queries[x][1])] = -1
                elif t1 ==0 and t2!=0:
                    ans.append(abs(n-queries[x][0]))
                    dicts[(queries[x][0],queries[x][1])] = abs(n-queries[x][0])
                elif t2==0 and t1!=0:
                    ans.append(abs(m-queries[x][0]))
                    dicts[(queries[x][0],queries[x][1])] =abs(m-queries[x][0])
                else:
                    ans.append(min(abs(m-queries[x][0]),abs(n-queries[x][0])))
                    dicts[(queries[x][0],queries[x][1])] = min(abs(m-queries[x][0]),abs(n-queries[x][0]))
                
        return ans

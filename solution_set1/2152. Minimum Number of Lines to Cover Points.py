##ss
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        
        giveit = {}
        
        for indx,(x,y) in enumerate(points):
            giveit[(x,y)] = indx
            
        #print(giveit)
        if len(points) in [1,2]:
            return 1
        
        def find_slope(pt1,pt2):
            arr1 = copy.deepcopy(pt1)
            arr2 = copy.deepcopy(pt2)
            arr1 = [int(x) for x in arr1]
            arr2 = [int(x) for x in arr2]
            #print(arr1,arr2)
            return (arr2[1] - arr1[1]) / (arr2[0] - arr1[0]) if (arr2[0] - arr1[0])!=0 else 10000
        
        def toarr(strs):
            return strs.split(",")
        
        def tostr(arr):
            return ",".join(arr)
        
        #memo = {}
        @lru_cache(None)
        def find_ans(arrnew):
            #print(arr)
            arr = copy.deepcopy(arrnew)
            
            arr = toarr(arr)
            if arrnew == "":
                return 0
            arr = [points[int(x)] for x in arr]
            
            if len(arr) == 0:
                return 0
            
            elif len(arr) in [1,2]:
                return 1
            
            #elif 
            else:
                ans = float('inf')
                for x in range(len(arr)):
                    
                    for y in range(x,len(arr)):
                        temp = ""
                        tempo = []
                        if x!=y:
                            slp = find_slope(arr[x],arr[y])
                            #cnt = 1
                            for z in range(len(arr)):
                                if z!=x and z!=y:
                                    if find_slope(arr[x],arr[z])!= slp:
                                        #cnt+=1
                                        xcor = arr[z][0]
                                        ycor = arr[z][1]
                                        
                                        if temp == "":
                                            #temp+=str(giveit[(xcor,ycor)])
                                            tempo.append(giveit[(xcor,ycor)])
                                        else:
                                            #temp+=','
                                            #temp+=str(giveit[(xcor,ycor)])
                                            tempo.append(giveit[(xcor,ycor)])
                            tempo = sorted(tempo)
                            tempo = [str(x) for x in tempo]
                            if len(tempo)!=0:
                                ans = min(ans, 1 + find_ans(",".join(tempo)))
                            else:
                                ans = min(ans, 1 + find_ans(temp))
                
                return ans
            
        return find_ans(tostr([str(x) for x in range(len(points))]))
        #print(memo)            
                        
        #return (memo[tostr([str(x) for x in range(len(points))])])
                        
        

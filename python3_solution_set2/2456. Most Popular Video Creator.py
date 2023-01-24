class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        dicts = {}

        for name,vid,view in zip(creators,ids,views):
            if name in dicts:
                dicts[name][0]+=view
                max_views = dicts[name][2]
                #print(max_views, view)
                if max_views < view:
                    dicts[name][1] = vid
                    dicts[name][2] = view
                elif max_views == view:
                    a = dicts[name][1]
                    b = vid
                    if len(a)!=len(b):
                        if len(a) > len(b):
                            if b == a[:len(b)]:
                                dicts[name][1] = b
                            else:
                                temp = [dicts[name][1]]
                                temp.append(vid)
                                temp.sort()
                                dicts[name][1] = temp[0]
                            
                        else:
                            if a == b[:len(a)]:
                                dicts[name][1] = a
                            else:
                                temp = [dicts[name][1]]
                                temp.append(vid)
                                temp.sort()
                                dicts[name][1] = temp[0]
                            

                    else:
                        temp = [dicts[name][1]]
                        temp.append(vid)
                        temp.sort()
                        dicts[name][1] = temp[0]
            else:
                dicts[name] = [view,vid,view]
                #print(dicts)
            

        arr = []

        for x in dicts:
            arr.append([x] + dicts[x])

        arr = sorted(arr, key = lambda x:(-x[1]))
        max_v = max([x[1] for x in arr])

        ans = []

        for a,b,c,d in arr:
            if b == max_v:
                ans.append([a,c])

        return ans

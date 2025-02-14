import pandas as pd

def valid(arr):
    for x in arr:
        if x[0] == '0':
            return False
        
        if int(x) > 255:
            return False
    
    return True

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    ans = {}

    for indx, r in logs.iterrows():
        ip = r['ip']
        ip = ip.split(".")
        if len(ip) != 4 or not valid(ip):
            ans[r['ip']] = ans.get(r['ip'],0) + 1
    
    res = [[x,ans[x]] for x in ans]
    res = sorted(res, key = lambda x:(x[1],x[0]), reverse=True)

    return pd.DataFrame(data=res, columns=['ip', 'invalid_count'])
    

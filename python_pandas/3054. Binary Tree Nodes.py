import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:

    outdeg = {}
    root = -1
    for indx,r in tree.iterrows():
        if pd.isnull(r['P']):
            root = r['N']
        outdeg[r['P']] = outdeg.get(r['P'],0) + 1

    ans = []
    cols = ['N', 'Type']

    for indx, r in tree.iterrows():
        if r['N'] in outdeg and r['N']!=root:
            ans.append([r['N'], 'Inner'])
        elif r['N'] == root:
            ans.append([r['N'], 'Root'])
        else:
            ans.append([r['N'], 'Leaf'])

    ans = sorted(ans, key = lambda x:x[0])
    return pd.DataFrame(data=ans, columns=cols)
    

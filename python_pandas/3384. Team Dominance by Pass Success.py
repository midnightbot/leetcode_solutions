import pandas as pd

def apply_half(x):
    [mins,seconds] = x.split(":")
    mins = int(mins)
    seconds = int(seconds)

    if (mins < 45) or (mins==45 and seconds==0):
        return 1
    else:
        return 2



def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    # print(teams[teams['player_id']==1]['team_name'][0])
    def team_name(player_id):
        ans =  teams[teams['player_id']==player_id]['team_name']
        return ans.iloc[0]

    passes['half'] = passes['time_stamp'].apply(apply_half)
    passes['team_a'] = passes['pass_from'].apply(team_name)
    passes['team_b'] = passes['pass_to'].apply(team_name)
    rows = []
    cols = ['team_name', 'half_number', 'dominance']
    keys = {}
    for indx, r in passes.iterrows():
        this_key = r['team_a'] + "," + str(r['half'])
        if r['team_a'] == r['team_b']:
            keys[this_key] = keys.get(this_key,0) + 1

        else:
            keys[this_key] = keys.get(this_key,0) - 1

    
    for k in keys:
        [team,half] = k.split(",")
        dominance = keys[k]
        rows.append([team,int(half),dominance])

    df = pd.DataFrame(data=rows, columns=cols)
    df_sorted = df.sort_values(by=['team_name', 'half_number'], ascending=[True, True])
    return df_sorted
    

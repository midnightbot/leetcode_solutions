import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    ans = []
    cols = ['user_id', 'email']

    for indx, r in users.iterrows():
        email = r['email']
        
        a_count = email.count('@')
        if a_count!=1:
            continue
        
        ends = False
        if len(email) >= 4 and email[-4:] == '.com':
            ends = True
        
        email = email.split("@")
        is_ok = True
        for i in email[0]:
            if i not in 'qwertyuiopasdfghjklzZxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_':
                # print(i)
                is_ok = False
                break
        
        for i in email[1][:-4]:
            if i not in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
                is_ok = False
                break
        # print(is_ok, ends, a_count, email)
        if is_ok and ends and a_count==1:
            ans.append([r['user_id'], r['email']])

    # print(ans)
    ans = sorted(ans, key = lambda x:x[0])
    return pd.DataFrame(data=ans, columns=cols)
    

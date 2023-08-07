import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    def email_check(str):
        temp = str.split('@')
        ans = True

        for indx, x in enumerate(temp[0]):
            if indx == 0:
                if x not in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
                    ans = False
            if x not in '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM_.-':
                ans = False

        return ans and len(temp)==2 and temp[1] == 'leetcode.com'


    ans = []

    for indx, r in users.iterrows():
        if email_check(r['mail']):
            ans.append(indx)

    return users.loc[ans]

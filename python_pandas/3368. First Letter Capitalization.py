import pandas as pd
def transform(strs):
    return strs.title()

def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['converted_text'] = user_content['content_text'].apply(transform)
    user_content = user_content.rename(columns={'content_text':'original_text'})
    return user_content
    

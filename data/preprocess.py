import pandas as pd

def drop_unnecessary_columns(data: pd.DataFrame):
    data = data.drop(['Unnamed: 0', 'flight'], axis=1)
    return data

def data_type_conversion(data: pd.DataFrame):
    stops_retype = {
        'zero': 0, 'one': 1, 'two_or_more': 2
    }
    object_cols = data.select_dtypes(include='object').columns
    object_cols = object_cols.drop('stops')
    data[object_cols] = data[object_cols].astype('category')

    if 'stops' in data.columns:
        data['stops'] = data['stops'].replace(stops_retype).astype('int64')

    return data
        
def handling_of_outliers(data: pd.DataFrame):
    
    pass

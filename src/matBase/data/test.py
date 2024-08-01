import pandas as pd

def test():


    # Example DataFrame
    df = pd.DataFrame({'A': [10, 20, 30],
                       'B': [40, 50, 60]})

    # Dictionary to add as a new feature
    data_dict = {"F1": [1, 2, 3]}

    # Convert dictionary to Pandas Series
    new_feature = pd.Series([1, 2, 3], name='F1')
    print(new_feature)
    # Add new feature to DataFrame
    df = df.assign(NewFeature=new_feature)

    return df

print(test())
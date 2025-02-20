import pandas as pd

def map_external_values_to_dataframe(df, column_name, external_values):
    df[column_name] = df[column_name].map(external_values)
    return df

# Example usage
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
external_values = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
df = map_external_values_to_dataframe(df, 'A', external_values)
print(df)

import pandas as pd

def retrieve_rows_containing_substring(df, column_name, substring):
    return df[df[column_name].str.contains(substring, na=False)]

# Example usage
data = {'A': ['apple', 'banana', 'cherry', 'date'], 'B': [1, 2, 3, 4]}
df = pd.DataFrame(data)
substring = 'an'
result = retrieve_rows_containing_substring(df, 'A', substring)
print(result)

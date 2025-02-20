import pandas as pd

def read_csv_file(filename):
    df = pd.read_csv(filename)
    return df

def print_first_and_last_five_lines(df):
    print("First five lines:")
    print(df.head())
    print("\nLast five lines:")
    print(df.tail())

filename = input("Enter the CSV filename: ")
df = read_csv_file(filename)
print_first_and_last_five_lines(df)

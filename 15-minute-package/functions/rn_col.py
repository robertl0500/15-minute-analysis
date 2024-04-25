import pandas as pd

def rename_column(df, old, new):
    df.rename(columns={old: new}, inplace=True)

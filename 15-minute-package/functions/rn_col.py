# Usage: rename_column(df, old='old_column', new='new_column'); Quick way to rename columns of dataframes

import pandas as pd

def rename_column(df, old, new):
    df.rename(columns={old: new}, inplace=True)

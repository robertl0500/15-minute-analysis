# Usage: duplicate_columns(gdf1, gdf2); Prints duplicate columns

def duplicate_columns(df1, df2):
    
    col_1 = set(df1.columns)
    col_2 = set(df2.columns)
    
    duplicate_columns = col_1.intersection(col_2)
    
    if duplicate_columns:
        print("Duplicate column names found:")
        for column_name in duplicate_columns:
            print(f"- {column_name}")
    else:
        print("No duplicate column names found.")
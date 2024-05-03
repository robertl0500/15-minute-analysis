def unique_columns(df1, df2):
    
    col_1 = set(df1.columns)
    col_2 = set(df2.columns)
    
    unique_columns = col_1.symmetric_difference(col_2)
    
    if unique_columns:
        print("Unique column names found:")
        for column_name in unique_columns:
            print(f"- {column_name}")
    else:
        print("No unique columns; all columns are duplicates.")
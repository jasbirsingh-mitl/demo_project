import pandas as pd

# 1. Read the Excel file
df=pd.read_csv( r"C:\Users\jasbir.singh02\OneDrive - Motherson Group\Desktop\student_performance.csv",index_col="student_id")

print(df.size)
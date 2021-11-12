import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
complete_cols, complete_rows, incomplete_cols = ([] for i in range(3))

#print(df.head())
for col in df.columns:
    if (df[df[col].isnull()].index.tolist() == []):
        complete_cols.append(col)
    else:
        incomplete_cols.append(col)

all_df = df[df[df.columns].notnull().all(axis=1)]
empty_val_df= df[df[df.columns].isnull().all(axis=1)]

all_df.to_csv('complete.csv')
empty_val_df.to_csv('incomplete.csv')

print(complete_cols)

# for index,row in df.iterrows():
#     complete = True
#     for col in incomplete_cols:
#         if str(row[col]) == '':
#             complete = False
#             break
#     if complete:
#         complete_rows.append(row['Country Name'])



# print('complete columns', complete_cols)
# print('complete rows', complete_rows)
# print('incomplete columns', incomplete_cols)

#print(df.isnull().sum())

#print(df[df.isnull().any(axis=1)])

# print(df.isnull().values.any(axis=1).sum())
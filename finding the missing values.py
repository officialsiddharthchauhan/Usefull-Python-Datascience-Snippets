# Importing libraries
# source  https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\fifa19\data.csv')

# Take a look at the first few rows
print(df.head())
print(df.isnull().values.any()) # to check if there is any missing value
# Detecting strings in the Potential column since its a numeric value 
cnt=0
for row in df['Club']:
    try:
        int(row)
        df.loc[cnt, 'Club']=np.nan
    except ValueError:
        pass
    cnt+=1

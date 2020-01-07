# Importing libraries
import pandas as pd
import numpy as np
#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b 
# Read csv file into a pandas dataframe
df = pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\fifa19\data.csv')

# Take a look at the first few rows

# Detecting strings in the Potential column since its a numeric value 
cnt=0
for row in df['Potential']:
    try:
        int(row)
        df.loc[cnt, 'Potential']=np.nan
    except ValueError:
        pass
    cnt+=1

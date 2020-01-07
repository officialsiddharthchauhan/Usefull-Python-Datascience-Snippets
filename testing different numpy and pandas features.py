# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:28:05 2019

@author: Admin
"""

#different function testing 
import numpy as np
import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\fifa19\data.csv')
Age=np.array(df['Age'])
print(df['Age'].max())
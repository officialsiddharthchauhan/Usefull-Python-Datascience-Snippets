# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:03:37 2019

@author: Admin
"""

#replacing the missing values
# Replace missing values with a number
df['ST_NUM'].fillna(125, inplace=True)
# Location based replacement
df.loc[2,'ST_NUM'] = 125
# Replace using median 
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True
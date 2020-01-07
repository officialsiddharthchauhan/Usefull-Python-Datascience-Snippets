# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:07:19 2019

@author: Admin

"""
#grouping the players by age
import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\fifa19\data.csv')
players_grp=df.groupby('Age')
print(players_grp.first())
print(players_grp.get_group(20))
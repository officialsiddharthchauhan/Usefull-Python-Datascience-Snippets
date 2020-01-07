import pandas as pd
file1=pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\datasets\life.csv')
file2=pd.read_csv(r'C:\Users\Admin\Desktop\datascience stuff\datasets\employ.csv')
def variable_correlation(var1,var2):
    both_up= (var1>var1.mean()) & (var2>var2.mean())
    both_down=(var1<var1.mean()) & (var2<var2.mean())
    is_same_direction=both_up | both_down
    num_same_direction=is_same_direction.sum()
    diff_direction=len(var1)-num_same_direction
    return(num_same_direction,diff_direction)
    
life_values=pd.Series(file1['2000'])
gdp_values=pd.Series(file2['2000'])
print(variable_correlation(life_values,gdp_values))
print(gdp_values.describe())
print(life_values.describe())
    
    
    
import unicodecsv

def read_csv(filename):
    with open(filename,'rb') as f:
        reader=unicodecsv.DictReader(f)   
        return list(reader)

data =read_csv(r'C:\Users\Admin\Desktop\datascience stuff\Project Iris\iris.csv')
print(data[2])
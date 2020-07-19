import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set= pd.read_csv('general_data.csv')

data_set.head()

data_set.isnull()
data_set.duplicated()
data_set.dropna()
data_set.drop_duplicates()

data_set.columns
data_set.drop(['Over18','StandardHours','EmployeeCount'],axis=1,inplace=True)
data_set.drop(['EmployeeID'],axis=1,inplace=True)
data_all=data_set.describe().T

att_dat1=data_set[data_set['Attrition']=='Yes'].head(101)
att_dat2=data_set[data_set['Attrition']=='No'].head(1001)

box=data_set.Age

plt.boxplot(box)

plt.show()

data1=att_dat1.describe().T
data2=att_dat2.describe().T
data1
data2

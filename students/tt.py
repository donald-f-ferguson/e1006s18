import pandas as pd

import pandas as pd
import numpy as np



data=pd.read_csv("AAPL.csv")
data3=0

# You had initialized this with '' which caused the list to start with a string.
list=[]

#total= data.index
#print(total)

adj_closes= data['Adj Close']

for i in range(1,len(adj_closes)):
    data1 = adj_closes[i-1]
    data2 = adj_closes[i]
    data3= (data2-data1)/data1
    list.append(data3)


num=len(list)
value = 0

for i in range(0,num):
        value=value + list[i]

print("average = ", value/(len(list)))